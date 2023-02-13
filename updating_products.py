import requests

url = "http://localhost:5000/products/{}".format(product_id)
data = {"name": "New product name", "price": 123.45}

response = requests.put(url, json=data)

if response.status_code == 200:
    print("Product successfully updated")
else:
    print("Could not update product")