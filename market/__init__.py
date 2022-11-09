# create a flask application
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#this is the path to the database file
#URI is a uniform resource identifier
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db=SQLAlchemy(app)



# create a model that will be a table in the database market.db

from market import routes,models