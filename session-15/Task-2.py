# Build a Flipkart-style price-per-item calculator: take total cart amount and item count as input, perform division, and use try-except to catch and display a user-friendly message if the item count is zero.

def price_per_item(c_amount, count):
    try:
        price = c_amount / count
    except ZeroDivisionError:
        print("Error: Number of items cannot be zero.")
    return price

# Test cases
c_amount = float(input("Enter the total cart amount: "))
count = int(input("Enter the number of items: "))
price_per_item(c_amount, count)