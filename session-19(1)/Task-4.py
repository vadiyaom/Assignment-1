# Extend the FoodOrder class by adding a method add_item(self, item_name, item_price) that adds the item to the items list and updates total_price. Demonstrate by adding two items to your order and printing the updated total.

class FoodOrder:

    def __init__(self, restaurant_name, items, total_price):
        self.restaurant_name = restaurant_name
        self.items = items
        self.total_price = total_price


    def add_item(self, item_name, item_price):
        self.items.append(item_name)
        self.total_price += item_price


    def __str__(self):
        return f"Restaurant Name: {self.restaurant_name}\nItems: {self.items}\nTotal Price: {self.total_price}"


my_order = FoodOrder("Dominos", ["Pizza"], 500)
my_order.add_item("Cold Drink", 50)
print(my_order)