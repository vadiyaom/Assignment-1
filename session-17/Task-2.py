# Write a script that uses the os module to create a new folder named 'MyDownloads' in your current working directory, then print the absolute path of the new folder.

import os

if os.path.exists("MyDownloads"):
    print("Folder alredy exist")
else:
    os.mkdir("MyDownloads")
    print("Folder created successfully")

