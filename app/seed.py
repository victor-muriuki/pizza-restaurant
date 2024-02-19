import random
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
        restaurant_names = ['Pizzeria Italia', 'Pizza Palace', 'Pizza Hut', 'Domino\'s Pizza', 'Little Caesars', 'California Pizza Kitchen', 'Papa John\'s Pizza', 'Sbarro', 'Blaze Pizza', 'Round Table Pizza']
        restaurant_addresses = ['123 Main St', '456 Elm St', '789 Oak St', '101 Pine St', '202 Maple St', '303 Cedar St', '404 Walnut St', '505 Cherry St', '606 Birch St', '707 Spruce St']
        for name, address in zip(restaurant_names, restaurant_addresses):
            restaurant = Restaurant(name=name, address=address)
            db.session.add(restaurant)
        db.session.commit()

        # Create Pizzas
        pizza_names = ['Margherita', 'Pepperoni', 'Vegetarian', 'Supreme', 'Hawaiian', 'Meat Lover\'s', 'BBQ Chicken', 'Buffalo Chicken', 'Mushroom', 'Sausage']
        pizza_ingredients = [
            'Tomato, Mozzarella, Basil',
            'Tomato, Mozzarella, Pepperoni',
            'Tomato, Mozzarella, Mushrooms, Bell Peppers, Olives',
            'Tomato, Mozzarella, Pepperoni, Sausage, Onions, Bell Peppers, Olives, Mushrooms',
            'Tomato, Mozzarella, Ham, Pineapple',
            'Tomato, Mozzarella, Pepperoni, Sausage, Bacon, Ham',
            'BBQ Sauce, Mozzarella, Grilled Chicken, Red Onions, Cilantro',
            'Buffalo Sauce, Mozzarella, Grilled Chicken, Red Onions, Ranch Drizzle',
            'Tomato, Mozzarella, Mushrooms, Parmesan, Garlic',
            'Tomato, Mozzarella, Sausage, Onions, Bell Peppers'
        ]
        for name, ingredients in zip(pizza_names, pizza_ingredients):
            pizza = Pizza(name=name, ingredients=ingredients)
            db.session.add(pizza)
        db.session.commit()

        # Create Restaurant-Pizza relationships with prices
        restaurants = Restaurant.query.all()
        pizzas = Pizza.query.all()
        for restaurant in restaurants:
            for pizza in pizzas:
                # Randomly generate a price between 8.99 and 15.99 for each pizza
                price = round(8.99 + (15.99 - 8.99) * random.random(), 2)
                restaurant_pizza = RestaurantPizza(restaurant_id=restaurant.id, pizza_id=pizza.id, price=price)
                db.session.add(restaurant_pizza)
        db.session.commit()

if __name__ == '__main__':
    seed_data()
    print("Data seeded successfully.")
