# Given a block of text containing multiple prices (like 'Rs. 299', 'Rs. 1500', etc.), use re.findall() to extract all the numeric price values as integers and print their sum.Look for patterns like 'Rs. ' followed by one or more digits.

import re

text = "I bought a shirt for Rs. 299, shoes for Rs. 1500 and a bag for Rs. 799."

prices = re.findall(r"Rs\.\s*(\d+)", text)

prices = [int(price) for price in prices]

total = sum(prices)

print("Prices:", prices)
print("Total:", total)