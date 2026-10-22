#Download a sample Instagram comments text file (or create your own with at least 10 lines), then write a Python script to extract all valid Instagram usernames (pattern: starts with '@', followed by letters, numbers, underscores, minimum 3 characters) using re.findall() and print the unique usernames.


import re

comments = """
Great post! Keep it up 👍 @samar_145 
Awesome content, totally agree! 
Thanks for sharing, @samar_145 
Love this! @anurag_132 
Nice pic 🔥 @photography_lover_2k23"""

usernames = re.findall(r"@[A-Za-z0-9_]{3,}", comments)

unique_usernames = sorted(list(set(usernames)))

print("Unique usernames:", unique_usernames)
