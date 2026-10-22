# Given a list of Zomato restaurant ratings [4.2, 3.8, 4.5, 2.9, 3.5], use filter() with a lambda to find and print only the restaurants with ratings above 4.0.

l1 = [4.2, 3.8, 4.5, 2.9, 3.5]

l2 = list(filter(lambda x: x >= 4.0, l1))
print(l2)