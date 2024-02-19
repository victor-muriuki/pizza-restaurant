import React, { useState } from 'react';
import axios from 'axios';

function AddRestaurantPizza() {
  const [price, setPrice] = useState('');
  const [pizzaId, setPizzaId] = useState('');
  const [restaurantId, setRestaurantId] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    
    // Check if price is within the valid range
    if (price < 1 || price > 30) {
      alert('Price must be between 1 and 30');
      return;
    }

    axios.post('/restaurant_pizzas', { price, pizza_id: pizzaId, restaurant_id: restaurantId })
      .then(response => {
        alert('Restaurant pizza added successfully');
        console.log('Restaurant pizza added successfully:', response.data);
        // Reset form fields
        setPrice('');
        setPizzaId('');
        setRestaurantId('');
      })
      .catch(error => {
        console.error('Error adding restaurant pizza:', error);
      });
  };

  return (
    <div>
      <h2>Add Restaurant Pizza</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Price:</label>
          <input type="text" value={price} onChange={(e) => setPrice(e.target.value)} />
        </div>
        <div>
          <label>Pizza ID:</label>
          <input type="text" value={pizzaId} onChange={(e) => setPizzaId(e.target.value)} />
        </div>
        <div>
          <label>Restaurant ID:</label>
          <input type="text" value={restaurantId} onChange={(e) => setRestaurantId(e.target.value)} />
        </div>
        <button type="submit">Add Restaurant Pizza</button>
      </form>
    </div>
  );
}

export default AddRestaurantPizza;
