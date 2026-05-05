import json

person = {
    "name": "Ahmad",
    "age": 30,
    "country": "Nigeria",
    "skills": ["Python", "Git", "Data Analysis"]
}

json_string = json.dumps(person)
print(json_string)
json_string = json.dumps(person, indent=4)
print(json_string)
json_data = '{"name":"Ahmad","age":30,"country":"Nigeria"}'

data = json.loads(json_data)
print(data)
print(data["name"])
with open("data.json", "w") as file:
    json.dump(person, file, indent=4)

with open("data.json", "r") as file:
    data = json.load(file)

print(data)
api_response = {
    "status": "success",
    "data": {
        "user": "Ahmad",
        "score": 95
    }
}

print(api_response["data"]["score"])