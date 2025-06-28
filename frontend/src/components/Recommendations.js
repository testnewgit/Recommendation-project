import React from 'react';

const Recommendations = ({ recommendations, isLoading }) => {
  if (isLoading) {
    return <p>Loading recommendations...</p>;
  }

  if (recommendations.length === 0) {
    return <p>No recommendations yet. Set preferences and browse some products.</p>;
  }

  return (
    <div>
      {recommendations.map((rec, index) => (
        <div key={index} className="recommendation-card">
          <h4>{rec.product.name}</h4>
          <p>₹{rec.product.price} – {rec.product.brand}</p>
          <p><strong>Why:</strong> {rec.explanation}</p>
        </div>
      ))}
    </div>
  );
};

export default Recommendations;
