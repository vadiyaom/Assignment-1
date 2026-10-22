# Create a text file named playlist.txt and write the names of 5 songs you listened to this week, each on a new line using Python's open() function in write mode.


f = open("playlist.txt", "w")

for i in range(5):
    song = input("Enter a song name: ")
    f.write(song + "\n")
