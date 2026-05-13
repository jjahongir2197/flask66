from flask import Flask, render_template, request, redirect

app = Flask(__name__)

products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Phone", "price": 600}
]

cart = []

@app.route("/")
def home():
    return render_template("index.html", products=products)

@app.route("/buy/<int:id>")
def buy(id):

    product = products[id]
    product["price"] *= 0.9  # 10% discount

    cart.append(product)

    return redirect("/cart")

@app.route("/cart")
def cart_page():

    total = sum(p["price"] for p in cart)

    return render_template("cart.html", cart=cart, total=total)

if __name__ == "__main__":
    app.run(debug=True)
