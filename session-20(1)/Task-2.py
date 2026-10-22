# Build a Product class for a Flipkart-style app with a private attribute _price. Implement get_price() and set_price() methods to access and update the price. Demonstrate setting and getting the price for a product object.

class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    
    def get_price(self):
        return self._price
    
    def set_price(self, price):
        self._price = price

my_product = Product("Product 1", 100)
print(my_product.get_price())
my_product.set_price(200)
print(my_product.get_price())

