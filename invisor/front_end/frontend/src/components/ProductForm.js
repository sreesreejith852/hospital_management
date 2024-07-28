// src/components/ProductForm.js

import React, { useState } from 'react';
import axios from 'axios';

const ProductForm = () => {
  const [productName, setProductName] = useState('');
  const [variants, setVariants] = useState([{ name: '', options: [''] }]);

  const handleVariantChange = (index, event) => {
    const newVariants = [...variants];
    newVariants[index][event.target.name] = event.target.value;
    setVariants(newVariants);
  };

  const handleOptionChange = (variantIndex, optionIndex, event) => {
    const newVariants = [...variants];
    newVariants[variantIndex].options[optionIndex] = event.target.value;
    setVariants(newVariants);
  };

  const addVariant = () => {
    setVariants([...variants, { name: '', options: [''] }]);
  };

  const addOption = (index) => {
    const newVariants = [...variants];
    newVariants[index].options.push('');
    setVariants(newVariants);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const data = { name: productName, variants: variants };
    try {
      await axios.post('http://localhost:8000/api/products/', data);
      alert('Product created successfully!');
    } catch (error) {
      console.error('There was an error creating the product!', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Product Name:</label>
        <input
          type="text"
          value={productName}
          onChange={(e) => setProductName(e.target.value)}
          required
        />
      </div>
      {variants.map((variant, index) => (
        <div key={index}>
          <label>Variant Name:</label>
          <input
            type="text"
            name="name"
            value={variant.name}
            onChange={(e) => handleVariantChange(index, e)}
            required
          />
          {variant.options.map((option, optionIndex) => (
            <div key={optionIndex}>
              <label>Option:</label>
              <input
                type="text"
                value={option}
                onChange={(e) => handleOptionChange(index, optionIndex, e)}
                required
              />
            </div>
          ))}
          <button type="button" onClick={() => addOption(index)}>Add Option</button>
        </div>
      ))}
      <button type="button" onClick={addVariant}>Add Variant</button>
      <button type="submit">Create Product</button>
    </form>
  );
};

export default ProductForm;
