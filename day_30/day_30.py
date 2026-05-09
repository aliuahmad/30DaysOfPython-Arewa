import requests

class GitHubAnalyzer:
    def __init__(self, username):
        self.username = username
        self.url = f"https://api.github.com/users/{username}"
        self.data = None

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            self.data = response.json()
        except requests.exceptions.RequestException as e:
            print("Error:", e)
            self.data = None

    def display_summary(self):
        if not self.data:
            print("No data available")
            return

        print("\nGitHub Profile Summary")
        print("----------------------")
        print("Username:", self.data.get("login"))
        print("Name:", self.data.get("name") or "Not Available")
        print("Repos:", self.data.get("public_repos"))
        print("Followers:", self.data.get("followers"))
        print("Following:", self.data.get("following"))
        print("Location:", self.data.get("location") or "Not Available")
        print("Bio:", self.data.get("bio") or "Not Available")
        print("Account created:", self.data.get("created_at"))


# MAIN PROGRAM (VERY IMPORTANT)
username = input("Enter GitHub username: ")

app = GitHubAnalyzer(username)
app.fetch_data()
app.display_summary()