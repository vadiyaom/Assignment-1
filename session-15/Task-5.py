# Write a function called safe_divide_for_zomato that takes two numbers (bill amount and number of people), uses try, except, else, and finally to divide the bill and print the result, print a custom error if division by zero, and always print 'Split calculation done' at the end.

def safe_divide_for_zomato(bill_amount, num_people):
    try:
        result = bill_amount / num_people
    except ZeroDivisionError:
        print("Error: Number of people cannot be zero.")
    else:
        print("Result: ", result)
    finally:
        print("Split calculation done")

bill_amount = float(input("Enter the bill amount: "))
num_people = int(input("Enter the number of people: "))
safe_divide_for_zomato(bill_amount, num_people)
