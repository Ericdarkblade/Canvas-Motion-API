import requests
import Motion_Canvas_API_Sync.Motion.secrets as secrets

api_key = secrets.api_key
secret_workspace_name = secrets.workspace_name


# Finds the workspace_id of a workspace in motion, provided a workspace name, and API KEY
def find_target_workspace_id(
    target_workspace_name: str = secret_workspace_name, *, api_key: str = api_key
) -> str:
    """_summary_

    Args:
        target_workspace_name (str, optional): The Workspace Name you want to identify. Defaults to sercet_workspace_name.
        api_key (str, optional): The API KEY for usemotion.com. Defaults to secret_api_key.

    Returns:
        str: Workspace ID
    """
    url = "https://api.usemotion.com/v1/workspaces"

    headers = {"Accept": "application/json", "X-API-Key": api_key}

    motion_workspaces = requests.get(url, headers=headers).json()

    for workspace in motion_workspaces["workspaces"]:
        if workspace["name"] == target_workspace_name:
            return workspace["id"]


if __name__ == "__main__":
    print(find_target_workspace_id())
