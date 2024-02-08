import requests
from Motion_Canvas_API_Sync.Motion import workspaces
import Motion_Canvas_API_Sync.Motion.secrets as secrets
from datetime import datetime
from priority import Priority
from settings import server


secret_api_key = secrets.api_key

# payload["labels"] = ["Imported Assignment"]


def create_task(
    dueDate: datetime,
    name: str,
    workspaceId: str,
    projectId: str = None,
    description: str = None,
    labels: [str] = None,
    *,
    autoScheduled: bool = True,
    duration="NONE",
    startDate: datetime = None,
    deadlineType: str = "HARD",
    schedule: str = "Work Hours",
    status: str = None,
    priority: Priority = Priority.MEDIUM,
    api_key: str = secret_api_key,
):
    """Adds a task to usemotion with direct task metadata, and an API Key
        Example ISO 8601 date: '2024-01-25T09:29:28-07:00'

    Args:
        dueDate (datetime): *REQUIRED* for scheduled tasks.
        name (str): Task Name *REQUIRED*
        workspaceId (str): Motion API Workspace ID *REQUIRED*.
        projectId (str): Motion API Project ID. Defaults to None.
        description (str, optional): Supports Github Markdown. Defaults to None.
        labels (str], optional): Label must exist in the workspace. Defaults to None.
        autoScheduled (bool, optional): If False Removes all Autoschedule Related Data. Defaults to True.
        duration (str, optional): May be 'None' 'REMINDER' or Z+ (postive int). Defaults to "NONE".
        startDate (datetime, optional): Optional Start Time for the Auto Scheduler. Defaults to None.
        deadlineType (str, optional): Must be "SOFT", "HARD", or "NONE". Defaults to "HARD".
        schedule (str, optional): Schedule Hours for API owner, must be "Work Hours" for other users. Defaults to "Work Hours".
        status (str, optional): Task Status, most workspaces default to 'Todo'. Defaults to None.
        priority (Priority, optional): Priority ENUM from Tasks class. Defaults to Priority.MEDIUM.
        api_key (str, optional): API Key for usemotion.com. Defaults to secret_api_key.
    """
    url = f"{server}/tasks"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-API-Key": api_key,
    }

    payload = {
        "dueDate": dueDate.isoformat(),
        "duration": duration,
        "status": status,
        "autoScheduled": {
            "startDate": startDate,
            "deadlineType": deadlineType,
            "schedule": schedule,
        },
        "name": name,
        "projectId": projectId,
        "workspaceId": workspaceId,
        "description": description,
        "priority": priority.value,
        "labels": labels,
    }

    if not autoScheduled:
        payload["autoScheduled"] = None
    if startDate:
        payload["startDate"] = startDate.isoformat()
    else:
        payload["autoScheduled"].pop("startDate")
    # payload = json.dumps(payload)  # Replaces None with Null
    motion_response = requests.post(url, json=payload, headers=headers).json()

    return payload, motion_response


if __name__ == "__main__":
    from pytz import timezone

    est = timezone("US/Eastern")
    dueDate = est.localize(datetime(2024, 2, 8, 14, 25, 20))
    payload, motion_response = create_task(
        dueDate=dueDate,
        name="First Python Implemented Task Creation",
        workspaceId=workspaces.get_id(),
    )

    print(f"{'#' * 10} Payload {'#' * 10}")
    print(payload)

    print(f"{'#' * 10} motion_response {'#' * 10}")
    print(motion_response)
