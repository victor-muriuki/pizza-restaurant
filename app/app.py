from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import Pizza, Restaurant, RestaurantPizza, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

class GetRestaurant(Resource):
    pass
    
class GetRestaurantById(Resource):
    pass


if __name__ == "__main__":
    app.run(port = 5555)
