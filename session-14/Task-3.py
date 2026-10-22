# Download a sample CSV file of IPL match scores (you can create your own with columns: match_id, team1, team2, winner) and write a Python script to read the file and print the winner of each match using the csv module.

import csv


with open("ipl_matches.csv", "r") as f:
    reader = csv.DictReader(f)

    for i in reader:
        print(f"{i['match_id']}: {i['winner']}")
        