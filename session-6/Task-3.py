food_prices = {
    "Pizza": 350,
    "Burger": 150,
    "Pasta": 250,
    "Sandwich": 120,
    "Paneer Tikka": 280
}

for item, price in food_prices.items():
    if price > 200:
        print(item, ":", "₹", price)