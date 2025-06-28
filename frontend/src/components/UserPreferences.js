import React from 'react';

const UserPreferences = ({ preferences, products, onPreferencesChange }) => {
  const uniqueCategories = [...new Set(products.map(p => p.category))];
  const uniqueBrands = [...new Set(products.map(p => p.brand))];

  const handleCheckboxChange = (type, value) => {
    const current = preferences[type];
    const updated = current.includes(value)
      ? current.filter(v => v !== value)
      : [...current, value];
    onPreferencesChange({ [type]: updated });
  };

  return (
    <div>
      <h3>Your Preferences</h3>

      {/* Price Range */}
      <div style={{ marginBottom: '1rem' }}>
        <strong>Price Range:</strong>
        <div>
          <select
            value={preferences.priceRange}
            onChange={(e) => onPreferencesChange({ priceRange: e.target.value })}
          >
            <option value="all">All</option>
            <option value="0-50">0 - 50</option>
            <option value="50-100">50 - 100</option>
            <option value="100+">100+</option>
          </select>
        </div>
      </div>

      {/* Categories */}
      <div style={{ marginBottom: '1rem' }}>
        <strong>Categories:</strong>
        <div>
          {uniqueCategories.map(cat => (
            <div key={cat}>
              <input
                type="checkbox"
                checked={preferences.categories.includes(cat)}
                onChange={() => handleCheckboxChange('categories', cat)}
              />
              {cat}
            </div>
          ))}
        </div>
      </div>

      {/* Brands */}
      <div style={{ marginBottom: '1rem' }}>
        <strong>Brands:</strong>
        <div>
          {uniqueBrands.map(brand => (
            <div key={brand}>
              <input
                type="checkbox"
                checked={preferences.brands.includes(brand)}
                onChange={() => handleCheckboxChange('brands', brand)}
              />
              {brand}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default UserPreferences;
