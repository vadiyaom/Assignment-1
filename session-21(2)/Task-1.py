# Use the requests library to send a POST request to https://jsonplaceholder.typicode.com/posts with a JSON payload containing a title, body, and userId, then print the response status code and JSON data.

import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title" : "hello",
    "body" : "my body",
    "userId" : 1
}

response = requests.post(url,json=payload)

print("Status code: ",response.status_code)
print("JSON data: ",response.json())