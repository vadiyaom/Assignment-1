#Send a POST request to https://jsonplaceholder.typicode.com/posts using requests.post() with the data: title='My First Post', body='Hello from Python!', userId=101, and print the status code and the returned JSON response.

import requests

url = "https://jsonplaceholder.typicode.com/posts"


data = {
    "title": "My First Post",
    "userId": 101,
    "body": "Hello from Python!"
}

response = requests.post(url, json=data)


print("Status Code: " + str(response.status_code))
print("JSON Response: " + str(response.json()))
