import requests

username = "aliuahmad"

url = f"https://api.github.com/users/{username}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("GitHub User Data\n")
    print("Username:", data.get("login"))
    print("Name:", data.get("name"))
    print("Public Repos:", data.get("public_repos"))
    print("Followers:", data.get("followers"))
    print("Following:", data.get("following"))
    print("Location:", data.get("location"))
    print("Bio:", data.get("bio"))
else:
    print("Failed to fetch data. Status code:", response.status_code)