# Given two lists — one with cricket team names and one with their IPL points — use zip() to pair each team with its points and print them in the format: 'Team: Mumbai Indians, Points: 18'.

l1 = ["MI", "CSK", "RCB", "SRH", "KKR"]
l2 = [18, 16, 14, 12, 10]

for i,j in zip(l1,l2):
    print("Team :",i," | Points :",j)