# Write a function show_final_price(item) that takes any Product or Electronics object and prints its name and the discounted price by calling get_discounted_price(). Demonstrate polymorphism by passing both a Product and an Electronics object to this function.


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def get_discounted_price(self):
        return self.price - (self.price * 10 / 100)


class Electronics(Product):
    def get_discounted_price(self):
        return self.price - (self.price * 20 / 100)


def show_final_price(item):
    print("Product Name:", item.name)
    print("Discounted Price:", item.get_discounted_price())



product = Product("Book", 100)
electronics = Electronics("Phone", 1000)

show_final_price(product)
show_final_price(electronics)
