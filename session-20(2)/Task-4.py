# Build a small script that fetches movies from the OMDB API (http://www.omdbapi.com/) by sending a GET request with query parameters: apikey='demo', s='Avengers'. Print the total number of results found.Pass the parameters using the params={} argument in requests.get().

import requests

url = "https://www.omdbapi.com/"

params = {
    "apikey": "18d7219c",
    "s": "Avengers"
}

response = requests.get(url, params=params)

data = response.json()

if data.get("Response") == "True":
    print("Total Results:", data.get("totalResults"))
else:
    print("Error:", data.get("Error"))