import json
import urllib.request

username = "torvalds"
url = f"https://api.github.com/users/{username}"

response = urllib.request.urlopen(url)
data = json.loads(response.read().decode('utf-8'))

print(data["login"])
print(data["public_repos"])
print(data.get("name"))
print(data.get("location"))
print(data.get("bio"))
report = f"""
GitHub Report
--------------
Username: {data.get('login')}
Repos: {data.get('public_repos')}
Followers: {data.get('followers')}
Location: {data.get('location') or 'Not Available'}
"""

print(report)