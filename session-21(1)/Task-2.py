# Now create a subclass called Electronics that inherits from Product and overrides the get_discounted_price() method to apply a 20% discount instead of 10%.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def get_discounted_price(self):
        return self.price - (self.price * 10 / 100)


class Electronics(Product):
    def get_discounted_price(self):
        return self.price - (self.price * 20 / 100)



name = input("Enter product name: ")
price = float(input("Enter product price: "))


product = Electronics(name, price)

print("Product Name:", product.name)
print("Original Price:", product.price)
print("Discounted Price:", product.get_discounted_price())