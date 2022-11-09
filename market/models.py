

#initialize the database
from market import db

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(30),unique=True,nullable=False)
    email_address=db.Column(db.String(50),unique=True,nullable=False)
    password_hash=db.Column(db.String(60),nullable=False)
    budget=db.Column(db.Integer,nullable=False,default=1000)
    items=db.relationship('Item',backref='owned_user',lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email_address}')"

class Item(db.Model):
    name=db.Column(db.String(30),unique=True,nullable=False)
    barcode=db.Column(db.String(12),unique=True,nullable=False)
    price=db.Column(db.Integer(),nullable=False)
    id=db.Column(db.Integer(),nullable=False,primary_key=True)
    description=db.Column(db.String(100),nullable=False)
    owner=db.Column(db.Integer(),db.ForeignKey('user.id')) #this is the foreign key