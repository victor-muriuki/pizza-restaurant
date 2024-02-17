import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Pizzas() {
  const [pizzas, setPizzas] = useState([]);

  useEffect(() => {
    axios.get('/pizzas')
      .then(response => {
        setPizzas(response.data);
      })
      .catch(error => {
        console.error('Error fetching pizzas:', error);
      });
  }, []);

  return (
    <div>
      <h2>Pizzas</h2>
      <ul>
        {pizzas.map(pizza => (
          <li key={pizza.id}>
            <strong>{pizza.name}</strong> - {pizza.ingredients}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Pizzas;
