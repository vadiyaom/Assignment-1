# Create a class called FoodOrder with attributes: restaurant_name, items (list), and total_price. Write an __init__() constructor to initialize these, then create an object representing your last Zomato or Swiggy order and print its details.

class FoodOrder:

    def __init__(self,restaurant_name,items,total_price):
        self.restaurant_name = restaurant_name
        self.items = items
        self.total_price = total_price


    def __str__(self):
        return f"Restaurant Name: {self.restaurant_name}\nItems: {self.items}\nTotal Price: {self.total_price}"


my_order = FoodOrder("Dominos", ["Pizza", "Cold Drink"], 500)
print(my_order)