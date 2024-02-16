from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    # Add other restaurant attributes as needed
    pizzas = db.relationship('Pizza', secondary='restaurant_pizza')

class Pizza(db.Model):
    __tablename__ = 'pizzas'
    id = db.Column(db.Integer, primary_key=True)
    # Add other pizza attributes as needed
    restaurants = db.relationship('Restaurant', secondary='restaurant_pizza')

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizza'
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), primary_key=True)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), primary_key=True)
    price = db.Column(db.Float)

    restaurant = db.relationship('Restaurant', backref='restaurant_pizzas')
    pizza = db.relationship('Pizza', backref='restaurant_pizzas')

    @db.validates('price')
    def validate_price(self, key, price):
        assert 1 <= price <= 30, "Price must be between 1 and 30."
        return price

