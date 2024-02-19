from flask import Flask
from models import db, Restaurant, Pizza, RestaurantPizza

# Create a Flask application instance
app = Flask(__name__)

# Configure your Flask application instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy extension with your Flask application instance
db.init_app(app)

def seed_data():
    with app.app_context():  # Set up the Flask application context
        # Create Restaurants
        restaurant1 = Restaurant(name='Pizzeria Italia', address='123 Main St')
        restaurant2 = Restaurant(name='Pizza Palace', address='456 Elm St')
        db.session.add(restaurant1)
        db.session.add(restaurant2)
        db.session.commit()

        # Create Pizzas
        pizza1 = Pizza(name='Margherita', ingredients='Tomato, Mozzarella, Basil')
        pizza2 = Pizza(name='Pepperoni', ingredients='Tomato, Mozzarella, Pepperoni')
        pizza3 = Pizza(name='Vegetarian', ingredients='Tomato, Mozzarella, Mushrooms, Bell Peppers, Olives')
        db.session.add(pizza1)
        db.session.add(pizza2)
        db.session.add(pizza3)
        db.session.commit()

        # Create Restaurant-Pizza relationships with prices
        restaurant_pizza1 = RestaurantPizza(restaurant_id=restaurant1.id, pizza_id=pizza1.id, price=10.99)
        restaurant_pizza2 = RestaurantPizza(restaurant_id=restaurant1.id, pizza_id=pizza2.id, price=12.99)
        restaurant_pizza3 = RestaurantPizza(restaurant_id=restaurant2.id, pizza_id=pizza2.id, price=11.99)
        restaurant_pizza4 = RestaurantPizza(restaurant_id=restaurant2.id, pizza_id=pizza3.id, price=13.99)
        db.session.add(restaurant_pizza1)
        db.session.add(restaurant_pizza2)
        db.session.add(restaurant_pizza3)
        db.session.add(restaurant_pizza4)
        db.session.commit()

if __name__ == '__main__':
    seed_data()
    print("Data seeded successfully.")
