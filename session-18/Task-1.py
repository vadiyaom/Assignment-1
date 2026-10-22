import re

# Use re.findall() to extract all valid phone numbers from a given string in the format '+91-XXXXXXXXXX' (e.g., '+91-9876543210'). Print the list of found numbers.

data = "call me at +91-9876543210"
result = re.findall(r"(\+91-)\d{10}",data)
print(result)