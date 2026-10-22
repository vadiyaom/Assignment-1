# Add a method play_preview(self) to the Song class that prints 'Playing 30-second preview of [title] by [artist]'. Call this method using the object you created.

class Song:

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def play_preview(self):
        print('Playing 30-second preview of', self.title, 'by', self.artist)


my_fav_song = Song("Shape of You", "Ed Sheeran")
my_fav_song.play_preview()

