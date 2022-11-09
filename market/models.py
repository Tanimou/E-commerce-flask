

#initialize the database
from market import db

class Item(db.Model):
    name=db.Column(db.String(30),unique=True,nullable=False)
    barcode=db.Column(db.String(12),unique=True,nullable=False)
    price=db.Column(db.Integer(),nullable=False)
    id=db.Column(db.Integer(),nullable=False,primary_key=True)
    description=db.Column(db.String(100),nullable=False)