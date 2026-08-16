# Write a Python function that takes a list of IPL team names and prints only those teams whose names are longer than 6 characters, skipping the rest using the continue statement.

def long_team_names(teams):
    for team in teams:
        if len(team) <= 6:
            continue
        print(team)


teams = ["Mumbai Indians", "Chennai Super Kings", "RCB", "Kolkata Knight Riders", "SRH"]
long_team_names(teams)
