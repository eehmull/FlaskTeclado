from flask import Flask, render_template, request

app = Flask(__name__)
transactions = []

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        print(request.form)
        transactions.append(( 
            request.form.get("date"),
            float(request.form.get("amount")),
            request.form.get("account")
        ))
    return render_template("form.html")


@app.route("/transactions")
def show_transactions():
    return render_template("transactions.html", entries=transactions)