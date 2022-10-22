# create a flask application
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/market")
def market():
    return "<p>Market page</p>"

@app.route("/market/<item>")
def item(item):
    return f"<p>Item page</p>{item}"


