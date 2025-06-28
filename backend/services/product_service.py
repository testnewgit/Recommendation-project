import json
from config import config

class ProductService:
    """
    Service to handle product data operations
    """

    def __init__(self):
        """
        Initialize the product service with data path from config
        """
        self.data_path = config['DATA_PATH']
        self.products = self._load_products()

    def _load_products(self):
        """
        Load products from the JSON data file
        """
        try:
            with open(self.data_path, 'r') as file:
                return json.load(file)
        except Exception as e:
            print(f"Error loading product data: {str(e)}")
            return []

    def get_all_products(self):
        """
        Return all products
        """
        return self.products

    def get_product_by_id(self, product_id):
        """
        Get a specific product by ID
        """
        for product in self.products:
            if product['id'] == product_id:
                return product
        return None

    def get_products_by_category(self, category):
        """
        Get products filtered by category
        """
        return [p for p in self.products if p['category'] == category]

    def filter_products_by_preferences(self, preferences):
        """
        Filter products based on price range, categories, and brands
        """
        filtered = self.products

        # Filter by categories
        if preferences.get("categories"):
            filtered = [p for p in filtered if p['category'] in preferences['categories']]

        # Filter by brands
        if preferences.get("brands"):
            filtered = [p for p in filtered if p['brand'] in preferences['brands']]

        # Filter by price range
        price_range = preferences.get("priceRange", "all")
        if price_range != "all":
            try:
                if price_range == "0-50":
                    filtered = [p for p in filtered if p['price'] <= 50]
                elif price_range == "50-100":
                    filtered = [p for p in filtered if 50 < p['price'] <= 100]
                elif price_range == "100+":
                    filtered = [p for p in filtered if p['price'] > 100]
            except:
                pass

        return filtered
