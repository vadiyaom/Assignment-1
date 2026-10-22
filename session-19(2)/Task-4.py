# Modify your GET request to https://jsonplaceholder.typicode.com/posts so it only fetches posts by userId=2 by passing the correct query parameter. Print the IDs of the returned posts.Use the 'params' argument in requests.get().

import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {"userId": 2}

response = requests.get(url, params=params)

data = response.json()

for post in data:
    print(post["id"])
