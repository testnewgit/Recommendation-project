import google.generativeai as genai
from config import config
import json
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LLMServiceError(Exception):
    """Custom exception for Gemini LLM service errors."""
    pass

class LLMService:
    def __init__(self):
        """Initializes Gemini API with provided credentials and settings."""
        try:
            genai.configure(api_key=config['GEMINI_API_KEY'])
            self.model_name = config.get('MODEL_NAME', 'gemini-1.5-pro')
            self.max_tokens = config.get('MAX_TOKENS', 1000)
            self.temperature = config.get('TEMPERATURE', 0.7)
            logger.info("Gemini LLM service initialized")
        except Exception as e:
            raise LLMServiceError(f"Initialization failed: {str(e)}")

    def generate_recommendations(self, user_preferences, browsing_history, all_products):
        """Generates recommendations using Gemini API based on preferences and history."""
        try:
            browsed_products = [p for p in all_products if p['id'] in browsing_history]
            prompt = self._create_prompt(user_preferences, browsed_products, all_products)

            model = genai.GenerativeModel(self.model_name)
            chat = model.start_chat()
            chat.send_message("You are a recommendation system AI.")
            response = chat.send_message(prompt)

            return self._parse_response(response.text, all_products)
        
        except Exception as e:
            logger.error(f"Gemini API error: {str(e)}")
            return {"recommendations": [], "error": str(e)}

    def _create_prompt(self, prefs, browsed, products):
        """Builds a detailed prompt for Gemini API using user data."""
        try:
            preferences = "\n".join(f"- {k}: {v}" for k, v in prefs.items())
            history = "\n".join(
                f"- {p['name']} (${p['price']}, {p['brand']})" for p in browsed
            )
            relevant = self._rank_products(products, prefs)[:20]
            catalog = "\n".join(
                f"- {p['name']} (ID: {p['id']}, ${p['price']}, {p['brand']}, {p['rating']})" 
                for p in relevant
            )

            return f"""
Based on the user's preferences and browsing history, recommend 5 diverse and relevant products from the catalog.

User Preferences:
{preferences}

Browsing History:
{history}

Available Products:
{catalog}

Return a JSON list like:
[
  {{
    "product_id": "prod123",
    "explanation": "Matches your interest in sportswear and budget range.",
    "score": 9
  }},
  ...
]
Only return the JSON array.
"""
        except Exception as e:
            raise LLMServiceError(f"Prompt creation failed: {str(e)}")

    def _rank_products(self, products, prefs):
        """Scores and sorts products based on preference matching."""
        def score(p):
            s = 0
            if prefs.get('categories') and p['category'] in prefs['categories']:
                s += 3
            if prefs.get('brands') and p['brand'] in prefs['brands']:
                s += 2
            if (pr := prefs.get('priceRange')) and pr != 'all':
                low, high = map(float, pr.split('-'))
                if low <= p['price'] <= high:
                    s += 2
            return s + p.get('rating', 0)

        return sorted(products, key=score, reverse=True)

    def _parse_response(self, response, products):
        """Extracts product matches from Gemini API's JSON response."""
        try:
            start, end = response.find('['), response.rfind(']') + 1
            json_data = json.loads(response[start:end])
            recs = []

            for item in json_data:
                prod = next((p for p in products if p['id'] == item['product_id']), None)
                if prod:
                    recs.append({
                        "product": prod,
                        "explanation": item.get("explanation", ""),
                        "confidence_score": item.get("score", 5)
                    })
            return {"recommendations": recs, "count": len(recs)}
        
        except Exception as e:
            logger.error(f"Response parse error: {str(e)}")
            return {"recommendations": [], "error": "Invalid LLM response"}
