# Create a Paytm cashback calculator that asks for total spend and number of offers applied, then divides spend by offers to show average cashback per offer. If the number of offers is zero, raise a custom exception called NoOffersApplied and display a custom error message.Define your own exception class by subclassing Exception.

class NoOffersApplied(Exception):
    pass

def cashback(total_cashback, num_offers):
    if num_offers == 0:
        raise NoOffersApplied("No offers applied.")
    return total_cashback / num_offers

total_cashback = float(input("Enter the total cashback: "))
num_offers = int(input("Enter the number of offers: "))
print(cashback(total_cashback, num_offers))