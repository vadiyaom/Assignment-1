# Create a Python program that asks the user to enter their Zomato order amount and checks if it is above 300; if yes, print 'Eligible for free delivery', else print 'Delivery charges apply'.

order_amount = int(input("Enter Your Amount:"))

if order_amount > 300:
    print("You are eligible for free delivery.")
else:
    print("Delivery charges apply.")