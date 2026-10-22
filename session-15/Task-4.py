# Refactor the following buggy code to handle exceptions correctly so it never crashes and always prints 'Thank you for using the calculator' at the end, even if an exception occurs:def calculate_average_rating(total_rating, num_reviews): return total_rating / num_reviews print(calculate_average_rating(500, 0))

def calculate_average_rating(total_rating, num_reviews):
    try:
        return total_rating / num_reviews
    except ZeroDivisionError:
        print("Error: Number of reviews cannot be zero.")
    finally:
        print("Thank you for using the calculator.")

print(calculate_average_rating(500, 0))
