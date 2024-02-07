import requests
from workspaces import Workspace
import secrets

api_key = secrets.api_key

url = "https://api.usemotion.com/v1/projects/projectId"

headers = {"Accept": "application/json", "X-API-Key": "123"}


class Project:
    {
        "id": "string",
        "name": "string",
        "description": "string",
        "workspaceId": "string",
        "status": {"name": "string", "isDefaultStatus": True, "isResolvedStatus": True},
    }

    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        workspaceId: str,
        status_name: str,
        status_default: bool,
        status_resolved: bool,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.workspaceId = workspaceId
        self.status_name = status_name
        self.status_default = status_default
        self.status_resolved = status_resolved

    response = requests.get(url, headers=headers)
