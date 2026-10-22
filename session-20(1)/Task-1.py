# Create a Python class called Playlist with a private attribute _songs (a list) and a public method add_song(song) to add a song title to the playlist. Print the playlist after adding 3 songs.

class Playlist:
    def __init__(self):
        self._songs = []
    
    def add_song(self, song):
        self._songs.append(song)
    
    def display_playlist(self):
        print(self._songs)

my_playlist = Playlist()
my_playlist.add_song("Song 1")
my_playlist.add_song("Song 2")
my_playlist.add_song("Song 3")
my_playlist.display_playlist()

