# Send a POST request to https://jsonplaceholder.typicode.com/posts to add a new playlist with fields: title, userId, and body. Print the status code and the JSON response. Use requests.post() and pass your data as a JSON payload.

import requests

url = "https://jsonplaceholder.typicode.com/posts"


data = {
    "title": "The Rock",
    "userId": 2,
    "body": "The Rock is a very good movie"
}

response = requests.post(url, json=data)


print(response.status_code)
print(response.json())
