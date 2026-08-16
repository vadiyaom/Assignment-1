# Write a short Python script that takes a scenario (like a list of recent Zomato orders vs a tuple of fixed IPL team names) and prints which one should use a list and which should use a tuple, explaining your choice in a comment.

# Scenario 1: List of recent Zomato orders
# order can be added or removed, so list use here.
recent_orders = ["Pizza", "Burger", "Cold Coffee", "Pasta"]


# Scenario 2: Tuple of fixed IPL team names
# team names are fixed and should not change, so tuple use here.
ipl_teams = ("Mumbai Indians", "Chennai Super Kings", "Royal Challengers Bangalore", "Kolkata Knight Riders")

print("Recent Orders:", recent_orders) # Lists are mutable and suitable for scenarios where the data might change
print("IPL Teams:", ipl_teams) # Tuples are immutable and suitable for scenarios where the data should remain constant