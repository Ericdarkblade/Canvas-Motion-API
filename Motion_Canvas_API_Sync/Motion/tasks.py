import requests
import Motion_Canvas_API_Sync.Motion.secrets as secrets

secret_api_key = secrets.api_key

# payload["labels"] = ["Imported Assignment"]


def create_task(
    dueDate: str,
    name: str,
    workspaceId: str,
    description: str = None,
    labels: [str] = None,
    *,
    autoScheduled: bool = True,
    duration="NONE",
    startDate: str = None,
    deadlineType: str = "HARD",
    schedule: str = "Work Hours",
    status: str = None,
    api_key: str = secret_api_key,
):
    url = "https://api.usemotion.com/v1/tasks"
    headers = {"Accept": "application/json", "X-API-Key": api_key}

    payload = {
        "dueDate": dueDate,
        "duration": duration,
        "autoScheduled": {
            "startDate": startDate,
            "deadlineType": deadlineType,
            "schedule": schedule,
        },
        "name": name,
        "workspaceId": workspaceId,
        "description": description,
        "status": status,
        "labels": labels,
    }
    if not autoScheduled:
        payload["autoScheduled"] = None

    print(payload)

    # motion_response = requests.get(url, headers=headers).json()
