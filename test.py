import requests

response = requests.get("http://localhost:5000/products/1")

if response.status_code == 200:
    try:
        product = response.json()
        print(product)
    except ValueError as e:
        print("Failed to parse response as JSON:", e)
        print("Response text:", response.text)
else:
    print("Request failed with status code:", response.status_code)
