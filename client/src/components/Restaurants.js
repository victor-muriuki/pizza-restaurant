import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

function Restaurants() {
  const [restaurants, setRestaurants] = useState([]);
  const [selectedRestaurant, setSelectedRestaurant] = useState(null);

  useEffect(() => {
    fetchRestaurants();
  }, []);

  const fetchRestaurants = () => {
    axios.get('http://localhost:5555/restaurants')
      .then(response => {
        setRestaurants(response.data);
      })
      .catch(error => {
        console.error('Error fetching restaurants:', error);
      });
  };

  const handleDeleteRestaurant = (id) => {
    axios.delete(`http://localhost:5555/restaurants/${id}`)
      .then(() => {
        // Remove the deleted restaurant from the state
        setRestaurants(restaurants.filter(restaurant => restaurant.id !== id));
        setSelectedRestaurant(null); // Clear the selected restaurant if deleted
      })
      .catch(error => {
        console.error('Error deleting restaurant:', error);
      });
  };

  const handleRestaurantClick = (restaurantId) => {
  const restaurant = restaurants.find(restaurant => restaurant.id === restaurantId);
  setSelectedRestaurant(restaurant);
};


  return (
    <div>
      <h2>List of Restaurants</h2>
      <ul>
        {restaurants.map(restaurant => (
          <li key={restaurant.id}>
            <button onClick={() => handleRestaurantClick(restaurant.id)}>
              {restaurant.name} - {restaurant.address}
            </button>
            {/* Delete button for each restaurant */}
            <button onClick={() => handleDeleteRestaurant(restaurant.id)}>Delete</button>
          </li>
        ))}
      </ul>
      {selectedRestaurant && (
  <div>
    <h3>Selected Restaurant</h3>
    <p>Name: {selectedRestaurant.name}</p>
    <p>Address: {selectedRestaurant.address}</p>
    <h3>Pizzas</h3>
    <ul>
      {selectedRestaurant.pizzas && selectedRestaurant.pizzas.map(pizza => (
        <li key={pizza.id}>
          {pizza.name} - {pizza.ingredients}
        </li>
      ))}
    </ul>
  </div>
)}

      {/* Button to navigate to the Pizzas component */}
      <Link to="/restaurant_pizzas">
        <button>Add Restaurant Pizza</button>
      </Link>
       {/* Button to navigate to the Pizzas component */}
       <Link to="/pizzas">
        <button>View Pizzas</button>
      </Link>
    </div>
  );
}

export default Restaurants;
