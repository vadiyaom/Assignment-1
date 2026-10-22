# Read the playlist.txt file you created and display each song name in uppercase letters using Python.

f = open("playlist.txt", "r")

for line in f:
    print(line.upper())