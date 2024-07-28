// src/components/StockManagement.js

import React, { useState } from 'react';
import axios from 'axios';

const StockManagement = () => {
  const [productId, setProductId] = useState('');
  const [variantId, setVariantId] = useState('');
  const [quantity, setQuantity] = useState(0);
  const [action, setAction] = useState('add'); // 'add' for purchasing, 'remove' for selling

  const handleSubmit = async (event) => {
    event.preventDefault();
    const url = action === 'add' ? 'http://localhost:8000/api/add-stock/' : 'http://localhost:8000/api/remove-stock/';
    const data = { product_id: productId, variant_id: variantId, quantity: quantity };
    try {
      await axios.post(url, data);
      alert(`Stock ${action === 'add' ? 'added' : 'removed'} successfully!`);
    } catch (error) {
      console.error(`There was an error ${action === 'add' ? 'adding' : 'removing'} the stock!`, error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Product ID:</label>
        <input
          type="text"
          value={productId}
          onChange={(e) => setProductId(e.target.value)}
          required
        />
      </div>
      <div>
        <label>Variant ID:</label>
        <input
          type="text"
          value={variantId}
          onChange={(e) => setVariantId(e.target.value)}
          required
        />
      </div>
      <div>
        <label>Quantity:</label>
        <input
          type="number"
          value={quantity}
          onChange={(e) => setQuantity(Number(e.target.value))}
          required
        />
      </div>
      <div>
        <label>Action:</label>
        <select value={action} onChange={(e) => setAction(e.target.value)}>
          <option value="add">Add Stock</option>
          <option value="remove">Remove Stock</option>
        </select>
      </div>
      <button type="submit">Submit</button>
    </form>
  );
};

export default StockManagement;
