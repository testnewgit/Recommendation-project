import React, { useState, useEffect } from 'react';
import './styles/App.css';
import Catalog from './components/Catalog';
import UserPreferences from './components/UserPreferences';
import Recommendations from './components/Recommendations';
import BrowsingHistory from './components/BrowsingHistory';
import { fetchProducts, fetchRecommendations } from './services/api';

function App() {
  const [products, setProducts] = useState([]);
  const [userPreferences, setUserPreferences] = useState({
    priceRange: 'all',
    categories: [],
    brands: []
  });
  const [browsingHistory, setBrowsingHistory] = useState([]);
  const [recommendations, setRecommendations] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    const loadProducts = async () => {
      try {
        const data = await fetchProducts();
        setProducts(data);
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    };

    loadProducts();
  }, []);

  const handleProductClick = (productId) => {
    if (!browsingHistory.includes(productId)) {
      setBrowsingHistory([...browsingHistory, productId]);
    }
  };

  const handlePreferencesChange = (newPreferences) => {
    setUserPreferences(prevPreferences => ({
      ...prevPreferences,
      ...newPreferences
    }));
  };

  const handleGetRecommendations = async () => {
    setIsLoading(true);
    try {
      const data = await fetchRecommendations(userPreferences, browsingHistory);
      setRecommendations(data.recommendations || []);
    } catch (error) {
      console.error('Error getting recommendations:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleClearHistory = () => {
    setBrowsingHistory([]);
  };

  return (
    <div className="app">
      <header className="app-header">
        <h1>AI-Powered Product Recommendation Engine</h1>
      </header>

      <main className="app-content">
        <div className="user-section">
          <UserPreferences 
            preferences={userPreferences}
            products={products}
            onPreferencesChange={handlePreferencesChange}
          />

          <BrowsingHistory 
            history={browsingHistory}
            products={products}
            onClearHistory={handleClearHistory}
          />

          <button 
            className="get-recommendations-btn"
            onClick={handleGetRecommendations}
            disabled={isLoading || browsingHistory.length === 0}
          >
            {isLoading ? 'Getting Recommendations...' : 'Get Personalized Recommendations'}
          </button>
        </div>

        <div className="catalog-section">
          <h2>Product Catalog</h2>
          <Catalog 
            products={products}
            onProductClick={handleProductClick}
            browsingHistory={browsingHistory}
          />
        </div>

        <div className="recommendations-section">
          <h2>Your Recommendations</h2>
          <Recommendations 
            recommendations={recommendations}
            isLoading={isLoading}
          />
        </div>
      </main>
    </div>
  );
}

export default App;
