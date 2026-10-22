# Write a script that fetches the latest 5 posts from https://jsonplaceholder.typicode.com/posts, parses the JSON response, and saves the post titles and userIds to a CSV file called posts.csv.<br><br><em><strong>Hint:</strong> Use the csv module for writing to CSV.</em>

import requests
import csv

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()

with open("posts.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "userId"])
    for post in data[:5]:
        writer.writerow([post["title"], post["userId"]])
