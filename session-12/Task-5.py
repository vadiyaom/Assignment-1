# Use an AI tool like ChatGPT or Copilot to generate a lambda function that filters out all odd numbers from a list of IPL scores [101, 98, 120, 77, 88], then test the code in your Python environment and paste the working code here.

l1 = [101, 98, 120, 77, 88]


l2 = list(filter(lambda x: x % 2 == 0, l1))
print(l2)
