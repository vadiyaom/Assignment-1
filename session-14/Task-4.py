import json

with open("movies.json", "r") as file:
    movies = json.load(file)

for movie in movies:
    print("Title:", movie["title"])
    print("Rating:", movie["rating"])