# create a flask application
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/market")
def market():
    return "<p>Market page</p>"

@app.route("/market/<item>")
def item(item):
    return f"<p>Item page</p>{item}"
