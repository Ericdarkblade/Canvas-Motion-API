import requests
import Motion_Canvas_API_Sync.Config.globals as globals


api_key = globals.api_key


def __init__():
    url = "https://api.usemotion.com/v1/workspaces"

    headers = {"Accept": "application/json", "X-API-Key": api_key}

    response = requests.get(url, headers=headers)

    return response


if __name__ == "__main__":
    print(__init__().json())