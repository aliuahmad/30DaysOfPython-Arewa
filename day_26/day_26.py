import requests
import json

# Convert Python → JSON
person = {
    "name": "Ahmad",
    "country": "Nigeria",
    "skills": ["Python", "Git", "APIs"]
}

json_data = json.dumps(person, indent=4)
print("Python to JSON:")
print(json_data)

print("\n-----------------\n")

# Convert JSON → Python
json_string = '{"city":"Abuja","population":3000000}'
python_data = json.loads(json_string)

print("JSON to Python:")
print(python_data["city"])

print("\n-----------------\n")

# Call GitHub API
response = requests.get("https://api.github.com/users/aliuahmad")
data = response.json()

print("GitHub API Data:")
print("Username:", data["login"])
print("Public repos:", data["public_repos"])
print("Followers:", data["followers"])


