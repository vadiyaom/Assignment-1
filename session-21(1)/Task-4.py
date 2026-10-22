# Build a simple Ticket class for a movie booking app with a method get_final_price(). Then, create a subclass PremiumTicket that overrides get_final_price() to add a 50 rupee convenience fee. Show both in action by creating objects and printing their final prices.Use super() in PremiumTicket to reuse the parent method and add the extra fee.


class Ticket:
    def __init__(self, cost):  
        self.price = cost

    def get_final_price(self):
        return self.price


class PremiumTicket(Ticket):
    def get_final_price(self):
        base = super().get_final_price()
        extra_fee = 50 
        total = base + extra_fee
        return total 


user_input_str = input("Enter ticket price: ")
price = float(user_input_str)

normal_ticket = Ticket(price)
premium_ticket = PremiumTicket(price)

print("Normal Ticket Price:", normal_ticket.get_final_price())
print("Premium Ticket Price:", premium_ticket.get_final_price())