from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Product 1",
        "price": 19.99
    },
    {
        "id": 2,
        "name": "Product 2",
        "price": 29.99
    },
    {
        "id": 3,
        "name": "Product 3",
        "price": 39.99
    }
]


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)


@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify(product)
    else:
        return "Product not found", 404


@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        data = request.get_json()
        product.update(data)
        return jsonify(product)
    else:
        return "Product not found", 404


if __name__ == "__main__":
    app.run()
