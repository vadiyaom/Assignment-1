# Create a function called get_delivery_charge(amount, city='Ahmedabad') that returns 0 if city is 'Ahmedabad', otherwise returns 50 as a delivery charge. Use a default argument for the city parameter.

def get_delivery_charge(amount, city='Ahmedabad'):
    if city == 'ahmedabad':
        return 0
    else:
        return 50

amount = int(input("Enter the amount: "))
city = input("Enter the city: ").lower()
print("The delivery charge is: ",get_delivery_charge(amount,city))
