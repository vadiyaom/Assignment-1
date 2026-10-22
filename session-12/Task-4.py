# Create a function format_followers that takes a number and returns it in 'K' or 'M' format (e.g., 1500 → '1.5K', 1200000 → '1.2M'), then use map() to apply it to a list of follower counts: [950, 1500, 25000, 1200000].


def format_followers(num):
    if num >= 1000000:
        return str(num / 1000000) + "M"
    elif num >= 1000:
        return str(num / 1000) + "K"
    else:
        return str(num)

followers = [950, 1500, 25000, 1200000]

formatted = list(map(format_followers, followers))

print(formatted)