# create a flask application
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#this is the path to the database file
#URI is a uniform resource identifier
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

#initialize the database
db=SQLAlchemy(app)

# create a model that will be a table in the database market.db
class Item(db.Model):
    name=db.Column(db.String(30),unique=True,nullable=False)
    barcode=db.Column(db.String(12),unique=True,nullable=False)
    price=db.Column(db.Integer(),nullable=False)
    id=db.Column(db.Integer(),nullable=False,primary_key=True)
    description=db.Column(db.String(100),nullable=False)

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



