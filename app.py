# app.py
from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/result", methods=["POST"])
def result():
    income = request.form["income"]
    age = request.form["age"]
    loan_amount = request.form["loanAmount"]
    credit_score = request.form["creditScore"]
    employment_status = request.form["employmentStatus"]

    # Placeholder prediction logic
    prediction = random.choice(["Likely to Default", "Unlikely to Default"])

    return render_template("result.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

