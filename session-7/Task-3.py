# Build a Python script that takes your Flipkart cart total and applies the following logic: if total > 2000, print 'You get a 10% discount'; elif total > 1000, print 'You get a 5% discount'; else print 'No discount available'.

total_amount = int(input("Enter Your Amount:"))
total = 0
if total_amount > 2000:
    discount = total_amount * 0.10
    print("You get a '10%'  discount")
elif total_amount > 1000:
    discount = total_amount * 0.5
    print("You get a 5% Discount")
else:

    print("No discount avalible")

total = total_amount - discount
print("Discount is:",discount)
print("Your total price after Discount is:",total)