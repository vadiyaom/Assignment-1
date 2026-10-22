# Use the requests library in Python to send a GET request to the public API https://jsonplaceholder.typicode.com/posts and print the titles of the first 5 posts.

import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)  

data = response.json()

for post in data[:5]:
    print(post["title"])