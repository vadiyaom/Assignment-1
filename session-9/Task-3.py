# Write a function called format_price(price, currency='INR') that returns a string like '₹500' if currency is 'INR', or '$500' if currency is 'USD'.

def format_price(price, currency='INR'):
    if currency == 'INR':
        return f'₹{price}'# ₹ ctrl+alt+4
    elif currency == 'USD':
        return f'${price}'
    else:
        return f'{currency} {price}'

price = int(input("Enter the price: "))
currency = input("Enter the currency: ").upper()
print(format_price(price, currency))

