# Create a Python class called Product with attributes name and price, and a method get_discounted_price() that returns the price after applying a 10% discount.

class Product:
    
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def get_discounted_price(self):
        dis = self.price *0.10
        return self.price-dis


product=Product("laptop",1000)
print(product.get_discounted_price())
