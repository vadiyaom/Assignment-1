# Use re.sub() to replace all email addresses in a string with '[hidden email]' and print the modified string.Do not use any external libraries except re.

import re

text = "Contact me at abc@gmail.com or xyz@yahoo.com for more information."

modified_text = re.sub(r'\S+@\S+\.\S+', '[hidden email]', text)

print(modified_text)