from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Pizza, Restaurant, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)