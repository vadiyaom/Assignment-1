# Given a list of daily step counts for a week, use a while loop to find and print the first day when you crossed 10,000 steps.Hint: Loop through the list and stop as soon as you find a value greater than 10,000.

step_counts = [8000, 9500, 11000, 7500, 12000, 9000, 13000]
day = 0
while day < len(step_counts):
    if step_counts[day] > 10000:
        print(f"Day {day + 1}: {step_counts[day]} steps")
        break
    day += 1