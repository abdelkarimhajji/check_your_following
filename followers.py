
import requests

def fetch_github_followers(username):
    url = f"https://api.github.com/users/{username}/followers"
    followers = []
    page = 1

    while True:
        response = requests.get(url, params={'page': page, 'per_page': 100})
        
        if response.status_code != 200:
            print(f"Failed to fetch followers. Status code: {response.status_code}")
            break
        
        page_followers = response.json()
        
        if not page_followers:
            break

        followers.extend(page_followers)
        
        page += 1

    if followers:
        print(f"Total followers of {username}: {len(followers)}")
        for follower in followers:
            print(f"- {follower['login']}")
    else:
        print(f"{username} has no followers.")

fetch_github_followers('abdelkarimhajji')
