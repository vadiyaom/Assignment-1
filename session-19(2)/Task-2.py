# Create a Python dictionary that represents a Zomato-style restaurant object with fields like name, location, cuisines, and ratings. Convert this dictionary to a JSON string using the json module and print the result.

import json

restaurant = {
    "name": "Barbeque Nation",
    "location": "Connaught Place, New Delhi",
    "cuisines": ["North Indian", "Barbecue", "Kebab"],
    "ratings": 4.5
}

restaurant_json = json.dumps(restaurant, indent=4)

print(restaurant_json)
