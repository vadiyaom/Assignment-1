# Build a simple shopping cart total calculator: Given a list of item prices from a Flipkart cart, use a loop to sum the prices. If an item price is 0 (out of stock), skip it. Stop adding items if the running total crosses ₹2000 using break, and print the final total.Use both break and continue in your solution.

item_prices = [500, 0, 1500, 200, 3000, 1000]
total = 0

for price in item_prices:
    if price == 0:
        continue
    total += price
    if total > 2000:
        break

print(f"Final total: ₹{total}")