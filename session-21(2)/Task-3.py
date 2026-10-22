# Send a POST request to https://reqres.in/api/users with a JSON object containing a username and job, then parse the response to extract and print the created user's ID and creation timestamp.Hint:Use response.json() to access the returned data.

import requests

url = "https://reqres.in/api/users"

payload = {
    "name" : "Sahil",
    "job" : "Data Analyst"
}

response = requests.post(url,json=payload)

print("User ID:",response.json()["id"])
print("Timestamp:",response.json()["createdAt"])