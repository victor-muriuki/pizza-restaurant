from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import Pizza, Restaurant, RestaurantPizza, db
from flask_migrate import Migrate
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)
api = Api(app)
migrate = Migrate(app, db)

# Parser for POST requests to /restaurant_pizzas
parser = reqparse.RequestParser()
parser.add_argument('price', type=float, required=True, help='Price is required')
parser.add_argument('pizza_id', type=int, required=True, help='Pizza ID is required')
parser.add_argument('restaurant_id', type=int, required=True, help='Restaurant ID is required')

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
        args = parser.parse_args()
        price = args['price']
        pizza_id = args['pizza_id']
        restaurant_id = args['restaurant_id']

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
    app.run(debug=True)