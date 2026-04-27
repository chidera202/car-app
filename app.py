from flask import Flask, render_template, request, jsonify
import stripe

app = Flask(name)

# 🔑 PUT YOUR STRIPE SECRET KEY HERE
stripe.api_key = "sk_test_XXXXXXXX"

# 🚗 CAR DATA (IMPORTANT: NO $ HERE)
cars = [
    {
        "id": 1,
        "name": "Toyota Camry 2010",
        "price": 5000,
        "image": "images/car1.jpg",
        "desc": "Clean car, nothing to fix"
    },
    {
        "id": 2,
        "name": "Honda Accord 2012",
        "price": 6200,
        "image": "images/car2.jpg",
        "desc": "Smooth engine, fuel efficient"
    }
]

@app.route("/")
def home():
    return render_template("index.html", cars=cars)

# 💳 STRIPE PAYMENT
@app.route("/create-checkout-session", methods=["POST"])
def create_checkout_session():
    data = request.json

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "usd",
                "product_data": {
                    "name": data["name"],
                },
                "unit_amount": int(data["price"]) * 100,
            },
            "quantity": 1,
        }],
        mode="payment",
        success_url="https://car-app-p82x.onrender.com/",
        cancel_url="https://car-app-p82x.onrender.com/",
    )

    return jsonify({"id": session.id})

if name == "main":
    app.run(debug=True)
