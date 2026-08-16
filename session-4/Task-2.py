# Given the product name ' OnePlus Nord-CE 3 ', write code to clean it by removing extra spaces, converting all letters to uppercase, and replacing the dash with a colon.Hint:Use strip(), upper(), and replace() methods in sequence.

product_name = " OnePlus Nord-CE 3 "

product_name = product_name.strip()
product_name = product_name.upper()
product_name = product_name.replace("-", ":")
print(product_name)

