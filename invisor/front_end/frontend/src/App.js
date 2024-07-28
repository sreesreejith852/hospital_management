// src/App.js

import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ProductForm from './components/ProductForm';
import ProductList from './components/ProductList';
import StockManagement from './components/StockManagement';

const App = () => {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/create">Create Product</a></li>
            <li><a href="/list">Product List</a></li>
            <li><a href="/stock">Manage Stock</a></li>
          </ul>
        </nav>
        <Routes>
          <Route path="/create" element={<ProductForm />} />
          <Route path="/list" element={<ProductList />} />
          <Route path="/stock" element={<StockManagement />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
