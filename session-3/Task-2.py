# Write a function total_cart_amount(prices) that takes a list of product prices as strings (like ['199.99', '49', '350.75']) and returns the total as a float. Print the result for a sample Flipkart-style cart. Use float() to convert each string before summing.


def total_cart_amount(prices):
    total = 0
    for price in prices:
        total += float(price)
    return total

cart_prices = ['199.99', '49', '350.75']
result = total_cart_amount(cart_prices)
print(f"Total Cart Amount: ₹{result}")