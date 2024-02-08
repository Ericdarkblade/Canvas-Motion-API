import json

payload = {
    "NonNullValue": "This is a data entry",
    "IntegerEntry": 20,
    "NullEntry": None,
}

print("Python Dictionary")
print(payload)

print("JSON format")
print(json.dumps(payload))

print(payload.NullEntry)