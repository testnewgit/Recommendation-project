# AI-Powered Product Recommendation Engine - Backend

This is the backend component of the AI-Powered Product Recommendation Engine. It provides a FastAPI API that interfaces with an LLM to generate personalized product recommendations based on user preferences and browsing history.

## Project Structure

```
backend/
│
├── app.py               # Main FastAPI application
├── requirements.txt     # Python dependencies
├── config.py            # Configuration (add your API keys here)
├── data/
│   └── products.json    # Sample product catalog
│
├── services/
│   ├── __init__.py
│   ├── llm_service.py   # Service for LLM interactions (implement this)
│   └── product_service.py  # Service for product data operations
│
└── README.md            # This file
```

## Setup Instructions

1. Create a virtual environment:
   ```
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the backend directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   MODEL_NAME=gpt-3.5-turbo
   MAX_TOKENS=1000
   TEMPERATURE=0.7
   DATA_PATH=data/products.json
   ```

5. Run the application:
   ```
   uvicorn app:app --host 0.0.0.0 --port 5000 --reload
   ```

The server will start on `http://localhost:5000`. You can access the automatic API documentation at `http://localhost:5000/docs`.

## API Endpoints

### GET /api/products
Returns the full product catalog.

#### Response
```json
[
  {
    "id": "prod001",
    "name": "Ultra-Comfort Running Shoes",
    "category": "Footwear",
    "subcategory": "Running",
    "price": 89.99,
    "brand": "SportsFlex",
    "description": "...",
    "features": ["..."],
    "rating": 4.7,
    "inventory": 45,
    "tags": ["..."]
  },
  ...
]
```

### POST /api/recommendations
Generates personalized product recommendations based on user preferences and browsing history.

#### Request Body
```json
{
  "preferences": {
    "priceRange": "all", // Options: "0-50", "50-100", "100+", "all"
    "categories": ["Electronics", "Home"], // Array of category names
    "brands": ["SoundWave", "FitTech"] // Array of brand names
  },
  "browsing_history": ["prod002", "prod007"] // Array of product IDs
}
```

#### Response
```json
{
  "recommendations": [
    {
      "product": {
        "id": "prod009",
        "name": "Bluetooth Portable Speaker",
        "category": "Electronics",
        "subcategory": "Audio",
        "price": 69.99,
        "brand": "SoundWave",
        "description": "...",
        "features": ["..."],
        "rating": 4.4,
        "inventory": 50,
        "tags": ["..."]
      },
      "explanation": "Based on your interest in audio devices and the SoundWave brand...",
      "confidence_score": 8
    },
    ...
  ],
  "count": 5
}
```




