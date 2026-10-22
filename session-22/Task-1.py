import requests

session = requests.Session()

url = "https://www.flipkart.com/account/orders"

response1 = session.get(url)
print("First request status:", response1.status_code)

response2 = session.get(url)
print("Second request status:", response2.status_code)

print("Cookies:", session.cookies)
print("Headers:", session.headers)