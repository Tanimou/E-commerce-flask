#Import the database object (db) from the main application module
#This will define our database and initialize the SQLAlchemy extension
from datetime import datetime
from market import db,bcrypt,login_manager
from flask_login import UserMixin

# This code loads a user from the database, using the user's id
# This code is used in the login form, to check whether the user exists in the database
# The function name is load_user
# The variable name is user_id
# The line of code is called in the login form, and it uses the user_id variable
# It returns the user object

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#Define a base model for other database tables to inherit
class Base(db.Model,UserMixin):

    __abstract__  = True

    id = db.Column(db.Integer, primary_key = True)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    date_modified = db.Column(db.DateTime, default = datetime.utcnow,
    onupdate = datetime.utcnow)

#Define a User model
class User(Base):

    # User Name
    username = db.Column(db.String(128),  nullable = False)

    # Identification Data: email & password
    email_address = db.Column(db.String(128),  nullable = False, unique = True)
    password_hash = db.Column(db.String(192),  nullable = False)

    # Define the relationship to the Item table
    items = db.relationship('Item', backref = 'owned_user',
                            lazy = 'dynamic')
    budget=db.Column(db.Integer,nullable=False,default=1000)

    # This code is used to generate a hash of the password. The hash is stored in the database 
    # and the password itself is not stored. When a user logs in, the password is hashed and 
    # compared to the hash in the database. If the hashes match, the password is correct.

    @property
    # This allows you to access the password attribute
    def password(self):
        # This is the getter
        return self.password
    @password.setter
    # This allows you to set the password attribute
    def password(self, password):
        # This is the setter
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        
    
        #create a function for checking the password 
    def check_password_correction(self,attempted_password):
        return bcrypt.check_password_hash(pw_hash=self.password_hash, password=attempted_password)
   
    def __repr__(self):
        return '<User %r>' % (self.name)

# Define the Item Data Model
class Item(Base):
    
    # Task Name
    name = db.Column(db.String(128),  nullable = False)

    # Identification Data: barcode & price
    barcode = db.Column(db.String(12),  nullable = False)
    price = db.Column(db.Integer,  nullable = False)

    # Item description
    description = db.Column(db.String(128),  nullable = False)

    # Define the relationship to the User table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Item %r>' % (self.name)


def init_db():
    # Clear the database
    db.drop_all()
    # Create the database and the database table
    db.create_all()
    # Commit the changes
    db.session.commit()

# This function creates a new user in the database.
def add_user(username, email, password):
    # Create a new User object
    user = User(username=username,email_address=email,password=password)
    # Add the new user to the database session
    db.session.add(user)
    # Commit the changes to the database
    db.session.commit()


# This function creates a new item with the provided parameters and adds it to the database session.
def add_item(name, barcode, price, description,owner): # define a function called add_item with parameters name, barcode, price, description, and owner
    item = Item(name=name,barcode=barcode, price=price,description=description,user_id=owner) # create a new Item with the provided parameters
    db.session.add(item) # add the new Item to the database session
    db.session.commit() # commit the changes to the database

def get_user(username):
    # Look up a user by their username.
    # Return the user object or None.
    return User.query.filter_by(username=username).first()

def get_item(barcode):
    # Query the database for an item with the given barcode
    return Item.query.filter_by(barcode=barcode).first()

def get_all_users():
    """
    gets all users from the database
    """
    return User.query.all()


def get_all_items():
    """Gets all the items in the database.

    Returns:
        list of Item. The list of items in the database.

    """
    return Item.query.all()


def delete_user(username):
    # Retrieve the user to be deleted
    user = get_user(username)

    # If the user does not exist, return None
    if not user:
        return None

    # Delete the user from the database
    try:
        user.delete()
    except Exception:
        return None

    # Return the deleted user
    return user


