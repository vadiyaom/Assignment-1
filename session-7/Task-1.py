# Write a Python script that takes your current Spotify listening time in minutes and checks if it is above 120 minutes; if yes, print 'You are a true music fan!', otherwise print 'Keep listening!'.

time = int(input("Enter listing time in minutes:"))

if time > 120:
    print("You are a true music fan!")
else:   
    print("Keep listening!")
    