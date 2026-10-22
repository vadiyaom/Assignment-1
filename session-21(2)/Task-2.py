# Build a Python script that lets a user enter a new playlist name and description, sends this data as JSON in a POST request to a mock API endpoint (such as https://jsonplaceholder.typicode.com/posts), and prints the playlist ID returned by the API.

import requests

url = "https://jsonplaceholder.typicode.com/posts"

playlist_name = input("Enter playlist name: ")
playlist_description = input("Enter playlist description: ")

payload = {
    "title" : playlist_name,
    "body" : playlist_description,
    "userId" : 1
}

response = requests.post(url,json=payload)

print("Playlist ID: ",response.json()["id"])

