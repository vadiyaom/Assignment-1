# Create a custom Python module called playlist_utils.py with a function add_song(playlist, song) that adds a song to a list. Import this module in another script and use it to add three songs to a playlist, then print the final playlist.


from modual.playlist_utils import add_song

playlist = []

add_song(playlist, "Shape of You")
add_song(playlist, "Shape of You")
add_song(playlist, "Shape of You")

print(playlist)