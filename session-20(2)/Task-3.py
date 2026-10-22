# Fetch a list of users from https://jsonplaceholder.typicode.com/users using requests.get(), then use the .json() method to extract and print the usernames of all users whose email ends with '.org'.

import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)


print("Status Code: " + str(response.status_code))

for user in response.json():
    if user["email"].endswith(".org"):
        print(user["username"])
        print(user["id"])