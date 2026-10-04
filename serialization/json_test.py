import json

user = {
    "name": "ewriq",
    "age": 2
}

data = json.dumps(user)

print(data)

data2 = data

user2 = json.loads(data2)

print(user2["name"])
print(user2["age"])