#Research using ChatGPT or Copilot to find out how to set custom HTTP headers (like 'Authorization') in a Python requests call. Write a short code snippet that sends a GET request to any API endpoint with a custom header and print the response status code.

import requests

url = "https://httpbin.org/anything"

headers = {
    "Authorization": "Bearer my_secret_token",
    "X-Custom-Header": "MyValue"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)