# Simulate removing the last played song from your playlist_ids list using pop(), and display the removed ID along with the remaining playlist.

playlist_ids = [101, 202, 303, 404, 505]
print(playlist_ids)
remove_song = playlist_ids.pop()

print(f"Remove Id : {remove_song}")
print(playlist_ids)