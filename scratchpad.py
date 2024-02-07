import json

payload = {
    "NonNull Value": "This is a data entry",
    "Integer Entry": 20,
    "Null Entry": None,
}

print("Python Dictionary")
print(payload)

print("JSON format")
print(json.dumps(payload))
