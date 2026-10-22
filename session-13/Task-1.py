# Write a recursive function in Python called print_playlist_songs(songs) that takes a list of song names (like a Spotify playlist) and prints each song name one by one using recursion.

def print_playlist_songs(songs):    
    if songs == []:
        return
    print(songs[0])
    print_playlist_songs(songs[1:])


songs = ["Shape of You", "Perfect", "Believer", "Faded", "Blinding Lights"]

print_playlist_songs(songs)
