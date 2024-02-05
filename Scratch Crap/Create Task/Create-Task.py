from distutils import dep_util
import requests
from datetime import datetime
from pytz import timezone
import pytz
import json

# API INFORMATION
url = "https://api.usemotion.com/v1/tasks"
api_key = "123"

# TIME MANAGEMENT INFORMATION
est = timezone("America/Indiana/Indianapolis")


payload = {
    "dueDate": "2024-01-25T09:29:28.166-07:00",
    "duration": "NONE",
    "autoScheduled": {
        "startDate": "2024-01-25",
        "deadlineType": "HARD",
        "schedule": "Work Hours",
    },
    "name": "string",  # Required
    "workspaceId": "string",  # Required
}
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-API-Key": api_key,
}

est_date = est.localize(datetime(2024, 2, 6, 14, 25))


description = "# Description Heading\nSample Text\n## Sample Heading2\nMore Sample Text"

payload["dueDate"] = est_date.isoformat()
payload["workspaceId"] = "Qn39qhPwj7mxfwT-zT-Po"
payload["name"] = "API Created Task for the Class Template"
payload["description"] = description
payload["status"] = "Todo"
payload["labels"] = ["Imported Assignment"]


with open("Scratch Crap/Create Task/create-task.json", "w") as write_file:
    payload_json = json.dump(payload, write_file, indent=4, sort_keys=True)

response = requests.post(url, json=payload, headers=headers)


with open("Scratch Crap/Create Task/create-task-response.json", "w") as write_file:
    payload_json = json.dump(response.json(), write_file, indent=4, sort_keys=True)
