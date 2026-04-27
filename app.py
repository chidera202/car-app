from flask import Flask, render_template

app = Flask(__name__)

cars = [
    {
        "name": "Toyota Camry 2010",
        "price": "$5,000",
        "image": "images/car1.jpg",
        "desc": "Clean car, nothing to fix"
    },
    {
        "name": "Honda Accord 2012",
        "price": "$6,200",
        "image": "images/car2.jpg",
        "desc": "Smooth engine, fuel efficient"
    }
]

@app.route("/")
def home():
    return render_template("index.html", cars=cars)

if __name__ == "__main__":
    app.run(debug=True)