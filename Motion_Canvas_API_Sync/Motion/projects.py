from typing import Any
import requests
import secrets
from priority import Priority
from datetime import datetime
from settings import server

api_key = secrets.api_key


headers = {"Accept": "application/json", "X-API-Key": "123"}


class Project:
    {
        "id": "string",
        "name": "string",
        "description": "string",
        "workspaceId": "string",
        "status": {"name": "string", "isDefaultStatus": True, "isResolvedStatus": True},
    }

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        return cls.__new__(cls, *args, **kwds)

    def __init__(
        self,
        project_response,
    ):
        self.id = (project_response["id"],)
        self.name = (project_response["name"],)
        self.description = (project_response["description"],)
        self.workspaceId = (project_response["workspaceId"],)
        self.status_name = (project_response["status"]["name"],)
        self.status_default = (project_response["status"]["default"],)
        self.status_resolved = (project_response["status"]["resolved"],)

    @classmethod
    def from_id(cls, id: str, workspaceId: str, api_key: str = api_key):
        url = f"{server}/projects/{id}"
        headers = {"Accept": "application/json", "X-API-Key": api_key}

        project = requests.get(url, headers=headers).json()

        if project["statusCode"] == 404:
            raise Exception(
                f"Project with id {id} does not exist in workspace with workspaceId {workspaceId}"
            )
        else:
            cls.__init__(project_response=project)

    @classmethod
    def from_name(cls, name: str, workspaceId: str, api_key: str = api_key):
        url = f"{server}/projects"

        headers = {"Accept": "application/json", "X-API-Key": api_key}
        querystring = {"workspaceId": workspaceId}
        projects = requests.get(url, headers=headers, params=querystring).json()

        for project in projects:
            if project["name"] == name:
                return cls.__init__(project_response=project)

        raise Exception(
            f"Project Name '{name}' Does Not Exist in workspace with id: {workspaceId}"
        )

    @classmethod
    def create(
        cls,
        name: str,
        workspaceId: str,
        dueDate: datetime = None,
        description: str = None,
        labels: [str] = None,
        status_name: str = None,
        priority: Priority = Priority.MEDIUM,
    ):
        url = f"{server}/projects"
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-API-Key": api_key,
        }
        payload = {
            "dueDate": None if dueDate is None else dueDate.isoformat(),
            "name": name,
            "workspaceId": workspaceId,
            "description": description,
            "labels": labels,
            "status": status_name,
            "priority": priority.value,
        }

        response = requests.post(url, json=payload, headers=headers)

        return cls.__init__(project_response=response)
