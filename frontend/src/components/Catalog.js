import React from 'react';

const Catalog = ({ products, onProductClick, browsingHistory }) => {
  return (
    <div className="catalog-grid">
      {products.map(product => {
        const isSelected = browsingHistory.includes(product.id);
        return (
          <div
            key={product.id}
            className={`product-card ${isSelected ? 'selected' : ''}`}
            onClick={() => onProductClick(product.id)}
          >
            <h4>{product.name}</h4>
            <p>{product.category} - {product.brand}</p>
            <p>₹{product.price}</p>
          </div>
        );
      })}
    </div>
  );
};

export default Catalog;
