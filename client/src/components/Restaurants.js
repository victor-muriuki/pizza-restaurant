import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Restaurants() {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    axios.get('/restaurants')
      .then(response => {
        setRestaurants(response.data);
      })
      .catch(error => {
        console.error('Error fetching restaurants:', error);
      });
  }, []);

  return (
    <div>
      <h2>Restaurants</h2>
      <ul>
        {restaurants.map(restaurant => (
          <li key={restaurant.id}>
            <strong>{restaurant.name}</strong> - {restaurant.address}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Restaurants;
