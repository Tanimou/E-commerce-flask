from market import app,db
from market.models import Item,User
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
    # db.drop_all()
    # db.create_all()
    #for g,h in enumerate(items):
     #   g=Item(name=h['name'],barcode=h['barcode'],price=h['price'],description=h['description'])
    #    db.session.add(g)
     #   db.session.commit()
    # u1=User(username='cisse',password_hash='cisse',email_address='cisse@live.fr')
    # db.session.add(u1)
    # db.session.commit()
    # i1=Item(name='laptop',barcode='123456789012',price=500,description='this is a laptop')
    # i2=Item(name='phone',barcode='123456789013',price=300,description='this is a phone')
    # db.session.add(i1)
    # db.session.commit()
    # db.session.add(i2)
    # db.session.commit()
    items=Item.query.all()
    item1=Item.query.filter_by(name='laptop').first()
    item1.owner=User.query.filter_by(username='cisse').first().id
    db.session.add(item1)
    db.session.commit()
    # db.session.rollback()
    return render_template("market.html",name=items)
