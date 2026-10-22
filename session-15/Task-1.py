# Write a Python function called get_song_duration_per_minute that divides the total duration of a Spotify playlist (in minutes) by the number of songs, and handles the case where the number of songs is zero using try, except, and finally blocks.



def get_song_duration_per_minute(playlist_duration, num_songs):
    try:
        duration_per_minute = playlist_duration / num_songs
    except ZeroDivisionError:
        print("Error: Number of songs cannot be zero.")
    finally:
        print("Task completed.")
    return duration_per_minute



# Test cases
print(get_song_duration_per_minute(100, 10))
print(get_song_duration_per_minute(100, 0))
