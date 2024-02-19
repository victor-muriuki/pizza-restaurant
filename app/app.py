from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Pizza, Restaurant, RestaurantPizza
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)


db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

# Parser for POST requests to /restaurant_pizzas
# parser = reqparse.RequestParser()
# parser.add_argument('price', type=float, required=True, help='Price is required')
# parser.add_argument('pizza_id', type=int, required=True, help='Pizza ID is required')
# parser.add_argument('restaurant_id', type=int, required=True, help='Restaurant ID is required')

class RestaurantsResource(Resource):
    def get(self):
        restaurants = Restaurant.query.all()
        restaurants_data = [{'id': restaurant.id, 'name': restaurant.name, 'address': restaurant.address} for restaurant in restaurants]
        return restaurants_data

class RestaurantResource(Resource):
    def get(self, id):
        restaurant = Restaurant.query.get(id)
        if restaurant:
            pizzas = [{'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients} for pizza in restaurant.pizzas]
            restaurant_data = {'id': restaurant.id, 'name': restaurant.name, 'address': restaurant.address, 'pizzas': pizzas}
            return restaurant_data
        else:
            abort(404, message="Restaurant not found")

    def delete(self, id):
        restaurant = Restaurant.query.get(id)
        if restaurant:
            RestaurantPizza.query.filter_by(restaurant_id=id).delete()
            db.session.delete(restaurant)
            db.session.commit()
            return '', 204
        else:
            abort(404, message="Restaurant not found")

class PizzasResource(Resource):
    def get(self):
        pizzas = Pizza.query.all()
        pizzas_data = [{'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients} for pizza in pizzas]
        return pizzas_data

class RestaurantPizzasResource(Resource):
    def post(self):
        price = request.form.get('price') or request.get_json().get('price')
        pizza_id = request.form.get('pizza_id') or request.get_json().get('pizza_id')
        restaurant_id = request.form.get('restaurant_id') or request.get_json().get('restaurant_id')

        if not price or not pizza_id or not restaurant_id:
            abort(400, message="Price, pizza ID, and restaurant ID are required.")

        try:
            price = float(price)
            pizza_id = int(pizza_id)
            restaurant_id = int(restaurant_id)
        except ValueError:
            abort(400, message="Price must be a number, and pizza and restaurant IDs must be integers.")

        restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(restaurant_pizza)
        try:
            db.session.commit()
            pizza = Pizza.query.get(pizza_id)
            if pizza:
                pizza_data = {'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients}
                return pizza_data, 201
            else:
                abort(404, message="Pizza not found")
        except:
            db.session.rollback()
            abort(400, message="Validation errors")
# Adding routes to the resources
api.add_resource(RestaurantsResource, '/restaurants')
api.add_resource(RestaurantResource, '/restaurants/<int:id>')
api.add_resource(PizzasResource, '/pizzas')
api.add_resource(RestaurantPizzasResource, '/restaurant_pizzas')

if __name__ == '__main__':
    app.run(debug=True, port = 5555)