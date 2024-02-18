// Restaurants.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Restaurants() {
  const [restaurants, setRestaurants] = useState([]);

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

  return (
    <div>
      <h2>List of Restaurants</h2>
      <ul>
        {restaurants.map(restaurant => (
          <li key={restaurant.id}>
            {restaurant.name} - {restaurant.address}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Restaurants;
