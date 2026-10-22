def get_unique_artists(spotify_playlist1, spotify_playlist2):
    return spotify_playlist1.union(spotify_playlist2)


spotify_playlist1 = {
    "Arijit Singh", "Shreya Ghoshal", "Armaan Malik"
}

spotify_playlist2 = {
    "Arijit Singh", "Neha Kakkar", "Sonu Nigam"
}

result = get_unique_artists(spotify_playlist1, spotify_playlist2)

print(result)