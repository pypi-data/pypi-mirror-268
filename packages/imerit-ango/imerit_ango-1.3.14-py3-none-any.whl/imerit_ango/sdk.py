import uuid
import zipfile
import urllib.request
from tqdm import tqdm
from urllib.parse import urlencode, urlparse, urlunparse
from imerit_ango.models.enums import Metrics, StorageFileTypes, ProjectRoles
from imerit_ango.models.invite import Invitation, RoleUpdate, ProjectMember
from imerit_ango.models.label_category import ToolCategory, ClassificationCategory, RelationCategory

import json
import requests
import logging
from typing import List, Dict, Any, Optional, Literal

from imerit_ango.models.storage import Storage

DEFAULT_HOST = "https://imeritapi.ango.ai"
HEADERS = {'Content-Type': 'application/json'}


class SDK:
    def __init__(self, api_key: str, host: str = DEFAULT_HOST):
        self.api_key = api_key
        self.host = host
        self.session = requests.Session()
        self.setup_logger()

    def setup_logger(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        # Configure logger as needed

    def make_request(self, method: str, endpoint: str, payload: Optional[Dict] = None) -> Any:
        """
        Make a network request and handle exceptions.
        :param method: HTTP method
        :param endpoint: API endpoint
        :param payload: Request payload
        :return: JSON response
        """
        url = self.host + endpoint
        headers = {**HEADERS, 'apikey': self.api_key}
        try:
            response = self.session.request(method, url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            self.logger.error(f"Error during request: {e}")
            return response.json().get('message', '')

    # Example refactored method using make_request
    def list_projects(self, page: int = 1, limit: int = 10) -> Dict:
        """
        List projects with pagination.
        :param page: Page number
        :param limit: Number of items per page
        :return: JSON response of projects list
        """
        endpoint = f"/v2/listProjects?page={page}&limit={limit}"
        return self.make_request("GET", endpoint)

    def get_project(self, project_id: str) -> Dict:
        """
        Get a specific project by ID.
        :param project_id: ID of the project
        :return: JSON response of the project
        """
        endpoint = f"/v2/project/{project_id}"
        return self.make_request("GET", endpoint)

    def get_tasks(self, project_id: str, page: int = 1, limit: int = 10, status: Optional[str] = None,
                  stage: Optional[str] = None, batches: Optional[List[str]] = None) -> Dict:
        """
        Get tasks for a specific project.
        :param project_id: ID of the project
        :param page: Page number
        :param limit: Number of items per page
        :param status: Filter tasks by status
        :param stage: Filter tasks by stage
        :param batches: Filter tasks by batches
        :return: JSON response of tasks
        """
        endpoint = f"/v2/project/{project_id}/tasks?page={page}&limit={limit}"
        if status:
            endpoint += f"&status[eq]={status}"
        if batches:
            endpoint += f"&batches={json.dumps(batches)}"
        if stage:
            endpoint += f"&stage={stage}"
        return self.make_request("GET", endpoint)

    def get_task(self, task_id: str) -> Dict:
        """
        Retrieve a specific task by its ID.
        :param task_id: ID of the task
        :return: JSON response of the task
        """
        endpoint = f"/v2/task/{task_id}"
        return self.make_request("GET", endpoint)

    def assign_task(self, project: str, tasks: List[str], stage_filter: str, email: str) -> Dict:
        """
        Assign a task to a user.
        :param project: Project ID
        :param tasks: List of task IDs
        :param stage_filter: Stage of the task
        :param email: Email of the user to whom the task is assigned
        :return: JSON response
        """
        endpoint = "/v2/task/assign"
        payload = {"project": project, "tasks": tasks, "user": email, "stage": stage_filter}
        return self.make_request("POST", endpoint, payload)

    def _get_upload_url(self, file_name: str, project: str, file_type: StorageFileTypes, storage_id: str = None):
        url = "%s/v2/getUploadUrl?name=%s&project=%s&type=%s" % (self.host, file_name, project, file_type.value)
        if storage_id:
            url += "&storageId=%s" % storage_id
        headers = {
            'apikey': self.api_key
        }
        r = self.session.get(url, headers=headers).json()
        url = r["data"]["uploadUrl"]
        return url

    def _get_signed_url(self, asset_url: str, project: str, file_type: StorageFileTypes, storage_id: str = None):

        url = "%s/v2/getSignedUrl?name=%s&project=%s&type=%s" % (self.host, asset_url, project, file_type.value)
        if storage_id:
            url += "&storageId=%s" % storage_id
        headers = {
            'apikey': self.api_key
        }
        r = self.session.get(url, headers=headers).json()
        url = r["data"]["signedUrl"]
        return url

    def __get_batches(self, project_id, batches):
        project_batches = self.get_batches(project_id)
        resp = []
        for b1 in batches:
            batch_exist = False
            for b2 in project_batches:
                if b1 == b2["_id"] or b1 == b2["name"]:
                    resp.append(b2["_id"])
                    batch_exist = True
            if not batch_exist:
                raise Exception("Batch %s not found" % b1)
        return resp

    def __check_storages(self, storage_id):
        resp = self.get_storages(storage_id=storage_id)
        storages_list = resp['data']['storages']
        storage_exists = False
        for t1 in storages_list:
            if '_id' in t1 and t1['_id'] == storage_id:
                storage_exists = True
        return storage_exists

    def upload_files_cloud(self, project_id: str, assets, storage_id: str = None, batches: List[str] = None):
        if storage_id and not self.__check_storages(storage_id):
            raise "Storage ID is Invalid!"
        url = "%s/v2/project/%s/cloud" % (self.host, project_id)

        project_batches = self.get_batches(project_id)

        def switch_batch_names_with_ids(batch_list, project_batch_list):
            resp = []
            for b1 in batch_list:
                batch_exist = False
                for b2 in project_batch_list:
                    if b1 == b2["_id"] or b1 == b2["name"]:
                        resp.append(b2["_id"])
                        batch_exist = True
                if not batch_exist:
                    raise Exception("Batch %s not found" % b1)
            return resp

        for a in assets:
            if storage_id:
                a['storage'] = storage_id
            if "batches" in a:
                a['batches'] = switch_batch_names_with_ids(a['batches'], project_batches)

        if batches:
            batch_ids = switch_batch_names_with_ids(batches, project_batches)
            url += "?batches=%s" % json.dumps(batch_ids)

        payload = json.dumps({"assets": assets})
        headers = {
            'Content-Type': 'application/json',
            'apikey': self.api_key
        }

        response = self.session.post(url, headers=headers, data=payload)
        return response.json()

    def upload_files(self, project_id: str, file_paths: List, storage_id: str = None, batches: List[str] = None):
        if storage_id and not self.__check_storages(storage_id):
            raise "Storage ID is Invalid!"
        assets = []
        for path in tqdm(file_paths):
            uid = uuid.uuid4().hex
            context_data = None
            metadata = None
            if isinstance(path, str):
                data = path
                external_id = uid
            else:
                data = path.get("data")
                external_id = path.get("externalId", uid)
                context_data = path.get("contextData", None)
                metadata = path.get("metadata", None)
            file = open(data, 'rb')
            fname = uid + '.' + file.name.split('.')[-1]
            url = self._get_upload_url(file_name=fname, project=project_id,
                                       file_type=StorageFileTypes.ASSET, storage_id=storage_id)
            requests.put(url, data=file.read())
            asset = {'data': url.split('?')[0],
                     'externalId': external_id,
                     'contextData': context_data,
                     'metadata': metadata}
            assets.append(asset)

        response = self.upload_files_cloud(project_id, assets, storage_id, batches)
        return response

    def create_issue(self, task_id: str, content: str, position: str) -> Dict:
        """
        Create an issue for a task.
        """
        endpoint = "/v2/issues"
        payload = {"content": content, "labelTask": str(task_id), "position": str(position)}
        return self.make_request("POST", endpoint, payload)

    def get_assets(self, project_id: str,
                   page: int = 1, limit: int = 10, filters:Dict= {}) -> Dict:
        """
        Retrieve assets for a project with optional filters.

        :param project_id: The ID of the project to retrieve assets from.
        :param page: The page number of the assets list.
        :param limit: The number of assets to return per page.
        :param filters: Additional filters as keyword arguments.
            possible filters are:
            {
                _id : str,
                externalId: str,
                isPreLabeled: bool,
                batches: ["<batch_id_1>", "<batch_id_2>"] #assets should have both this is not any query
            }
        :return: A dictionary representing the response from the API.
        """
        endpoint = f"/v2/project/{project_id}/assets?page={page}&limit={limit}&filters={json.dumps(filters)}"
        return self.make_request("GET", endpoint)

    def create_attachment(self, project_id: str, attachments: List[dict]) -> Dict:
        """
        Create attachments for a project.
        """
        endpoint = "/v2/attachments"
        payload = {"project": project_id, "attachments": attachments}
        return self.make_request("POST", endpoint, payload)

    def __generate_ndjson_iterator(self, content):
        """
        :param content: NDJSON content as a string
        :return: Iterator yielding each JSON object
        """
        for line in content.splitlines():
            if line:  # skip empty lines
                yield json.loads(line)

    def export(self, project_id: str, batches: List[str] = None, stage: str = None, export_format: str = "json",
               export_type=None, include_key_frames_only: bool = False, zip_file_path=None, filters=None) -> Any:
        """
        Export project data.
        """
        if filters is None:
            filters = {}
        return self.exportV3(project_id, batches, stage, export_format, export_type, include_key_frames_only,
                             zip_file_path, filters)

    def exportV3(self, project_id: str, batches: List[str] = None, stage: str = None, export_format: str = "json",
                 export_type=None, include_key_frames_only: bool = False, zip_file_path=None, filters=None):

        if filters is None:
            filters = {}

        params = {
            'sendEmail': 'false',
            'includeMetadata': 'true',
            'includeHistory': 'true',
            'includeSegmentationPoints': 'true',

            'doNotNotify': 'true',
            'project': project_id,
            'format': export_format,
            'type': export_type,
            'includeOnlyKeyFrames': str(include_key_frames_only).lower()
        }

        if batches:
            params['batches'] = json.dumps(batches)
        if stage:
            params['stage'] = json.dumps(stage)

        params.update(filters)

        url = f"{self.host}/v2/exportV3?{urlencode(params)}"
        headers = {'apikey': self.api_key}

        response = self.session.get(url, headers=headers)
        response.raise_for_status()  # raises an HTTPError if the response was an HTTP 4xx or 5xx

        link = response.json()['data']['exportPath']
        filehandle, _ = urllib.request.urlretrieve(link)

        if zip_file_path:
            urllib.request.urlretrieve(link, zip_file_path)
            pass
        else:
            with zipfile.ZipFile(filehandle, 'r') as zip_file_object:
                first_file = zip_file_object.namelist()[0]
                with zip_file_object.open(first_file) as file:
                    content = file.read()
                    if export_format == "ndjson":
                        json_response = self.__generate_ndjson_iterator(content), content.count(b'\n')
                    else:
                        json_response = json.loads(content)

            return json_response

    def create_label_set(self, project_id: str, tools: List[ToolCategory] = [],
                         classifications: List[ClassificationCategory] = [],
                         relations: List[RelationCategory] = [],
                         raw_category_schema: Dict = None) -> Dict:
        """
        Create a label set for a project.
        """
        endpoint = f"/v2/project/{project_id}"
        payload = {
            "categorySchema": {
                "tools": [t.toDict() for t in tools],
                "classifications": [c.toDict() for c in classifications],
                "relations": [r.toDict() for r in relations]
            }
        }
        if raw_category_schema:
            payload["categorySchema"] = raw_category_schema

        return self.make_request("POST", endpoint, payload)

    def import_labels(self, project_id: str, labels: List[dict]) -> Dict:
        """
        Import labels into a project.
        """
        endpoint = "/v2/import/labels"
        payload = {"project": project_id, "jsonContent": labels}
        return self.make_request("POST", endpoint, payload)

    def get_storages(self, storage_id: Optional[str] = None) -> Dict:
        """
        Retrieve storage information.
        """
        endpoint = "/v2/storages"
        if storage_id:
            endpoint += f"?_id={storage_id}"
        return self.make_request("GET", endpoint)

    def get_batches(self, project_id: str) -> List[Dict]:
        """
        Get batches for a project.
        """
        project_data = self.get_project(project_id)
        if 'data' in project_data:
            return project_data.get("data", {}).get("project", {}).get("batches", [])
        else:
            self.logger.error('Invalid Project Id!')
            return []

    def create_batch(self, project_id: str, batch_name: str) -> List[Dict]:
        """
        Create a new batch in a project.
        """
        endpoint = f"/v2/batches/{project_id}"
        batches = self.get_batches(project_id)
        payload = {"batches": batches + [{'name': batch_name}]}
        return self.make_request("POST", endpoint, payload)

    def assign_batches(self, project_id: str, asset_ids: List[str], batches: List[str]) -> Dict:
        """
        Assign batches to assets in a project.
        """
        endpoint = "/v2/assignBatches"
        payload = {"assets": asset_ids, "batches": batches}
        return self.make_request("POST", endpoint, payload)

    def create_project(self, name: str, description: str = "") -> Dict:
        """
        Create a new project.
        """
        endpoint = "/v2/project"
        payload = {"name": name, "description": description}
        return self.make_request("POST", endpoint, payload)

    def _annotate(self, task_id: str, answer: dict) -> bool:
        """
        Annotate a task with a given answer.
        """
        endpoint = f"/v2/annotate/{task_id}?nextStage=true"
        payload = {"answer": answer, "duration": 0}
        response = self.make_request("POST", endpoint, payload)
        return response is not None

    def update_workflow_stages(self, project_id: str, stages: List[dict]) -> Dict:
        """
        Update the workflow stages of a project.
        """
        endpoint = f"/v2/project/{project_id}"
        payload = {"stages": stages}
        return self.make_request("POST", endpoint, payload)

    def get_task_history(self, id: Optional[str] = None, task_id: Optional[str] = None) -> Dict:
        """
        Retrieve the history of a task.
        """
        if id:
            endpoint = f"/v2/taskHistory/{id}"
        elif task_id:
            endpoint = f"/v2/task/{task_id}/history"
        else:
            self.logger.error("id or task_id should be specified!")
            return {}
        return self.make_request("GET", endpoint)

    def get_metrics(self, project_id: str, metric: Metrics) -> Dict:
        """
        Retrieve metrics for a project.
        """
        endpoint = f"/v2/{project_id}/overview/{metric.value}"
        return self.make_request("GET", endpoint)

    def _plugin_response(self, response: Dict) -> Dict:
        """
        Handle plugin response.
        """
        endpoint = "/v2/pluginResponse"
        return self.make_request("POST", endpoint, response)

    def _plugin_log(self, log):
        endpoint = "/v2/pluginLog"
        return self.make_request("POST", endpoint, log)

    def get_organization_members(self, organization_id: str) -> Dict:
        """
        Get members of an organization.
        """
        endpoint = f"/v2/organization/{organization_id}/users"
        return self.make_request("GET", endpoint)

    def update_organization_members_role(self, organization_id: str, role_updates: List[RoleUpdate]) -> Dict:
        """
        Update organization members in bulk.
        """
        endpoint = f"/v2/organization/{organization_id}/users"
        members_dict = [member.toDict() for member in role_updates]
        payload = {"users": members_dict}
        return self.make_request("POST", endpoint, payload)

    def delete_organization_members(self, organization_id: str, member_emails: List[str]) -> Dict:
        """
        Delete members from an organization.
        """
        endpoint = f"/v2/organization/{organization_id}/users"
        payload = {"users": member_emails}
        return self.make_request("DELETE", endpoint, payload)

    def get_organization_invites(self, organization_id: str) -> Dict:
        """
        Get invites of an organization.
        """
        endpoint = f"/v2/organization/{organization_id}/invites?status=pending"
        return self.make_request("GET", endpoint)

    def invite_members_to_org(self, organization_id: str, invite_data: Invitation) -> Dict:
        """
        Invite a member to the organization.
        """
        endpoint = f"/v2/organization/{organization_id}/invites"
        return self.make_request("POST", endpoint, invite_data.toDict())

    def add_members_to_project(self, project_id: str, members: List[str], role: ProjectRoles) -> Dict:
        """
        Add a member to a project.
        """
        endpoint = f"/v2/project/{project_id}/assigned"
        payload = {"assignees": members, "role": role.value}

        return self.make_request("POST", endpoint, payload)

    def delete_organization_invites(self, organization_id: str, invite_emails: List[str]) -> Dict:
        """
        Delete invites from an organization with email.
        """
        endpoint = f"/v2/organization/{organization_id}/invites"
        payload = {"invites": invite_emails}
        return self.make_request("DELETE", endpoint, payload)

    def create_storage(self, storage_data: Storage) -> Dict:
        """
        Create a new storage.
        """
        endpoint = "/v2/storages/"
        return self.make_request("POST", endpoint, storage_data.to_dict())

    def delete_storage(self, storage_id: str) -> Dict:
        """
        Delete a specific storage.
        """
        endpoint = f"/v2/storages/{storage_id}"
        return self.make_request("DELETE", endpoint)

    def file_explorer(self, bucket: str, storage_id: str, options: Dict = {}) -> Dict:
        """
        options = {
            folder: 'path/to/folder',
            files: ['file1.txt', 'file2.jpg'],
            upload: false,
            projectId: 'your-project-id',
            scrollToken: null,
            batches: []
            extensions: []
            }
            """
        endpoint = f"/v2/file-explorer"

        body = options
        body['bucket'] = bucket
        body['storageId'] = storage_id

        return self.make_request("POST", endpoint, body)
