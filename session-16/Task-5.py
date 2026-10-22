# Create a generator function called order_id_generator that yields a new order ID (starting from 1001) each time it's called, similar to how Zomato or Swiggy generates unique order numbers. Use the yield statement inside a loop to generate the next ID.

def order_id_generator():
    i = 1001
    while True:
        yield i
        i += 1

o1 = order_id_generator()

print(next(o1))
print(next(o1))
print(next(o1))
print(next(o1))
print(next(o1))