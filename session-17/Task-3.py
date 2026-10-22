# Use the datetime module to get the current date and time, then format and print it as 'DD-MM-YYYY HH:MM:SS', similar to how WhatsApp shows message timestamps.Hint: Use strftime() to format the output.

import datetime

time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(time)