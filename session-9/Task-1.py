# Define a function called calculate_final_price(price, discount_rate) that returns the final price after applying the discount rate to the given price.

def calculate_final_price(price, discount_rate):
    discount = price * (discount_rate / 100)
    final_price = price - discount
    return final_price

price = int(input("Enter the price: "))
discount_rate = float(input("Enter the discount rate: "))

print("The final price is: ",calculate_final_price(price, discount_rate))