import requests

url = "https://api.usemotion.com/v1/workspaces"

api_key = "123"
headers = {"Accept": "application/json", "X-API-Key": api_key}

response = requests.get(url, headers=headers)

print(response.json())
