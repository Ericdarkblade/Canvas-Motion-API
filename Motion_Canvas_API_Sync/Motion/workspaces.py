import requests
import json
import Motion_Canvas_API_Sync.Motion.secrets as secrets


api_key = secrets.api_key
target_workspace_name = secrets.workspace_name


def find_target_workspace_id(target_workspace_name=target_workspace_name):
    url = "https://api.usemotion.com/v1/workspaces"

    headers = {"Accept": "application/json", "X-API-Key": api_key}

    motion_workspaces = requests.get(url, headers=headers).json()

    for workspace in motion_workspaces['workspaces']:
        if workspace['name'] == target_workspace_name:
            return workspace['id']

if __name__ == "__main__":
    print(find_target_workspace_id())