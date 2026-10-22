# Refactor your Song class so that the duration attribute is optional in the constructor (default to 0 if not provided).Use a default argument for duration in the __init__() method.

class Song:
    
    def __init__(self, title, artist, duration = 0):
        self.title = title
        self.artist = artist
        self.duration = duration


my_song = Song("Shape of You", "Ed Sheeran")
my_song2 = Song("Shape of You", "Ed Sheeran", 234)
print(my_song)
print(my_song2)
