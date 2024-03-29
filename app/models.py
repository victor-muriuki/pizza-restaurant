#models.py

from sqlalchemy.orm import validates
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()
# 


class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    address = db.Column(db.String(255))
    

    #relationships
    restaurant_Pizza = db.relationship('RestaurantPizza', backref = 'restaurants')
    pizzas = db.relationship('Pizza', secondary='restaurant_pizza', backref ='restaurants')


class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    ingredients = db.Column(db.String(255))

    restaurant_pizza = db.relationship('RestaurantPizza', backref ='pizzas')

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizza'

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), primary_key=True)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), primary_key=True)
    price = db.Column(db.Float)

    # restaurant = db.relationship('Restaurant', back_populates='pizzas')
    # pizza = db.relationship('Pizza', back_populates='restaurants')

    @validates('price')
    def validate_price(self, key, price):
        assert 1 <= price <= 30, "Price must be between 1 and 30."
        return price