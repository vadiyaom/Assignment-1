# Write a Python function using re.search() that checks if a string contains a valid date in the format 'DD/MM/YYYY'. The function should return True if a date is found, otherwise False.

import re

def check_date(date_str):
    pattern = r"^\d{2}/\d{2}/\d{4}$"
    if re.search(pattern, date_str):
        return True
    else:
        return False
print(check_date("28/08/2026"))
