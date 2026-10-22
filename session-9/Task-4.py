# Build a function called apply_coupon(price, coupon_code=None) that returns the price after a 10% discount if coupon_code is 'ZOMATO10', otherwise returns the original price.Constraint: Use a default argument for coupon_code._

def apply_coupon(price, coupon_code=None):
    if coupon_code == 'ZOMATO10':
        return price - (price * 0.10)
    else:
        return price

price = int(input("Enter the price: "))
coupon_code = input("Enter the coupon code: ").upper()
print("The final price is: ",apply_coupon(price, coupon_code))
