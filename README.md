# pizza-restaurant

## Introduction

This project is a web application that allows users to view restaurant and pizzas. Users can perform some operations like  (Read, add and Delete) on pizzas, restaurants and addrestaurantspizza through a user-friendly interface.

## Features

- restaurants Management: Users can view a list and delete from restaurants .
- pizzas Management: Users can view a list of pizzas.
- addrestaurantspizza Associations: Users can create new associations.

## Technologies Used

# frontend:

- React: JavaScript library for building user interfaces.
- React Router: Declarative routing for React applications.
- HTML/CSS: Markup and styling for the frontend.

# Backend:

- Flask: Micro web framework for building Python web applications.
- Flask-Restful: Extension for building REST APIs with Flask.
- SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- SQLite: Lightweight relational database management system.
Other Tools:
- Git: Version control system for tracking changes in the project.
- Postman: Tool for testing APIs and making HTTP requests.
- VS Code: Integrated development environment (IDE) for writing code.

## Setup Instructions

- Clone the Repository:  git clone <git@github.com:victor-muriuki/pizza-restaurant.git>

- Install Dependencies:
Navigate to the project directory: <cd pizza-restaurant>, <code .>

- Install frontend dependencies:  <cd client>
                <npm install>

- Install backend dependencies: <cd ..> , <cd app>
    <pipenv install flask>
    <pipenv install flask-migrate>
    <pipenv install flask-sqlalchemy >
    <pipenv install flask-restful>
   <pipenv install flask-cors>

- Run the Application:
    Start the backend server: <python3 app.py>

- Start the frontend development server: <cd client>
    <npm start>

- Access the Application:
Open your web browser and go to http://localhost:3000 to access the application.

## API Endpoints

- api.add_resource(RestaurantsResource, '/restaurants')
- api.add_resource(RestaurantResource, '/restaurants/<int:id>')
- api.add_resource(PizzasResource, '/pizzas')
- api.add_resource(RestaurantPizzasResource, '/restaurant_pizzas')

## License

This project is licensed under the Apache-2.0 license