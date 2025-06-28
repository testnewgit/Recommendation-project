import React from 'react';

const BrowsingHistory = ({ history, products, onClearHistory }) => {
  const viewedProducts = products.filter(p => history.includes(p.id));

  return (
    <div className="history-container">
      <h3>Your Browsing History</h3>
      {viewedProducts.length > 0 ? (
        <ul>
          {viewedProducts.map(product => (
            <li key={product.id}>{product.name} - ₹{product.price}</li>
          ))}
        </ul>
      ) : (
        <p>No products viewed yet.</p>
      )}
      {viewedProducts.length > 0 && (
        <button onClick={onClearHistory}>Clear History</button>
      )}
    </div>
  );
};

export default BrowsingHistory;
