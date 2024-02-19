import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Restaurants() {
  const [restaurants, setRestaurants] = useState([]);
  const [selectedRestaurant, setSelectedRestaurant] = useState(null);

  useEffect(() => {
    // Define your backend endpoint URL
    const backendEndpoint = 'http://localhost:5555/restaurants';

    // Fetch restaurant data from the backend
    axios.get(backendEndpoint)
      .then(response => {
        // Set the fetched restaurant data in the state
        setRestaurants(response.data);
      })
      .catch(error => {
        console.error('Error fetching restaurant data:', error);
      });
  }, []); // Run this effect only once when the component mounts

  // Function to handle when a restaurant is clicked
  const handleRestaurantClick = (restaurantId) => {
    // Define your endpoint URL for fetching specific restaurant data
    const restaurantEndpoint = `http://localhost:5555/restaurants/${restaurantId}`;

    // Fetch specific restaurant data from the backend
    axios.get(restaurantEndpoint)
      .then(response => {
        // Set the fetched restaurant data in the state
        setSelectedRestaurant(response.data);
      })
      .catch(error => {
        console.error('Error fetching specific restaurant data:', error);
      });
  };

  return (
    <div>
      <h2>List of Restaurants</h2>
      <ul>
        {restaurants.map(restaurant => (
          <li key={restaurant.id}>
            {/* Make each restaurant clickable */}
            <button onClick={() => handleRestaurantClick(restaurant.id)}>
              {restaurant.name} - {restaurant.address}
            </button>
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
            {selectedRestaurant.pizzas.map(pizza => (
              <li key={pizza.id}>
                {pizza.name} - {pizza.ingredients}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default Restaurants;
