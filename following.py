import requests

def fetch_github_following(username):
    url = f"https://api.github.com/users/{username}/following"
    following = []
    page = 1

    while True:
        response = requests.get(url, params={'page': page, 'per_page': 100})
        
        if response.status_code != 200:
            print(f"Failed to fetch following. Status code: {response.status_code}")
            break
        
        page_following = response.json()
        
        if not page_following:
            break

        following.extend(page_following)
        
        page += 1

    if following:
        print(f"Total following of {username}: {len(following)}")
        for user in following:
            print(f"- {user['login']}")
    else:
        print(f"{username} is not following anyone.")

fetch_github_following('abdelkarimhajji')
