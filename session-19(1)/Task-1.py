# Define a Python class called Song with attributes title, artist, and duration (in seconds). Create an object for your favorite song and print its details.

class Song:
    
    def __init__(self,title,artist,duration):
        self.title = title
        self.artist = artist
        self.duration = duration


my_fav_song = Song("Shape of you", "Ed Sheeran", 234)
print("Title: ",my_fav_song.title)
print("Artist: ",my_fav_song.artist)
print("Duration: ",my_fav_song.duration)
