import requests

#add product method by POST method
url = "http://localhost:5000/products"

headers = {
    "Content-Type": "application/json"
}

data = {
    "name": "Product 4",
    "price": 49.99
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
    print("Product created successfully")
else:
    print("Failed to create product")
# print(response.status_code)
