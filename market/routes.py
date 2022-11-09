from market import app
from market.models import Item
from flask import render_template
@app.route("/")
@app.route("/home")
def home_page():
#    db.create_all()
    return render_template("home.html")

@app.route("/market/<name>")
@app.route("/market")
def market():
    #the query.all() method returns a list of all the items in the database
    items=Item.query.all()
    #for g,h in enumerate(items):
     #   g=Item(name=h['name'],barcode=h['barcode'],price=h['price'],description=h['description'])
    #    db.session.add(g)
     #   db.session.commit()
    return render_template("market.html",name=items)
