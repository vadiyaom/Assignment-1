# Write a generator function called playlist_generator that takes a list of song names and yields each song one at a time, simulating a Spotify playlist shuffle.

def playlist_generator(l1):
    for i in l1:
        yield i

l1 = ["song1", "song2", "song3", "song4", "song5"]

g = playlist_generator(l1)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))