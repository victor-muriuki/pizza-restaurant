import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Restaurants from './components/Restaurants';
import Restaurant from './components/Restaurant';
import Pizzas from './components/Pizzas';
import AddRestaurantPizza from './components/AddRestaurantPizza';

function App() {
  return (
    <Router>
      <div className="App">
        <header>
          <h1>Restaurant App</h1>
        </header>
        <main>
          <Routes>
            <Route path="/" element={<Restaurants />} />
            <Route path="/restaurants" element={<Restaurants />} />
            <Route path="/restaurants/:id" element={<Restaurant />} />
            <Route path="/pizzas" element={<Pizzas />} />
            <Route path="/add-restaurant-pizza" element={<AddRestaurantPizza />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
