# Given the variable is_premium = 'True' (as a string), write code to correctly convert it to a boolean value and print its type. The bool() function alone won’t work as expected. Think about string comparison.</em>
is_premium = 'True'
is_premium_bool = is_premium == 'True'
print(f"Is Premium: {is_premium_bool} (Type: {type(is_premium_bool)})")