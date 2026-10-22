# Modify your script to save the same API data (latest 5 posts from https://jsonplaceholder.typicode.com/posts) into a JSON file named posts.json instead of CSV.

import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

data = response.json()

latest_posts = data[:5]

with open("posts.json", "w") as file:
    json.dump(latest_posts, file, indent=4)

print("Latest 5 posts saved successfully in posts.json")