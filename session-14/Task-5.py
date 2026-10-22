from pathlib import Path
import json

file_path = Path("my_fav_apps.json")

if not file_path.exists():
    apps = [
        {
            "name": "Instagram",
            "category": "Social Media"
        },
        {
            "name": "Zomato",
            "category": "Food Delivery"
        },
        {
            "name": "Paytm",
            "category": "Finance"
        }
    ]

    with open(file_path, "w") as file:
        json.dump(apps, file, indent=4)

    print("my_fav_apps.json created successfully")
else:
    print("my_fav_apps.json already exists")