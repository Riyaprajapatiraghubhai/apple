from flask import Flask, render_template

app = Flask(__name__)

products = [
    {"id": 1, "name": "iPhone 15 Pro", "price": "$999", "image": "https://via.placeholder.com/300x200"},
    {"id": 2, "name": "Apple Watch Series 9", "price": "$499", "image": "https://via.placeholder.com/300x200"},
    {"id": 3, "name": "Samsung Galaxy S24", "price": "$899", "image": "https://via.placeholder.com/300x200"},
    {"id": 4, "name": "Garmin Venu 3", "price": "$399", "image": "https://via.placeholder.com/300x200"}
]

@app.route('/')
def index():
    return render_template("index.html", products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((item for item in products if item["id"] == product_id), None)
    return render_template("product.html", product=product)

if __name__ == "__main__":
    app.run(debug=True)
