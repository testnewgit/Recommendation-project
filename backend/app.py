from fastapi import FastAPI, HTTPException, Request, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

from services.llm_service import LLMService
from services.product_service import ProductService
from config import config

app = FastAPI(title="AI Product Recommendation API")

# Enable CORS for all domains (you can restrict in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
product_service = ProductService()
llm_service = LLMService()

# Request models
class UserPreferences(BaseModel):
    priceRange: str = "all"
    categories: List[str] = []
    brands: List[str] = []

class RecommendationRequest(BaseModel):
    preferences: UserPreferences
    browsing_history: List[str] = []

# Product Catalog with Filtering & Sorting

@app.get("/api/products")
async def get_products(
    category: Optional[str] = Query(None, description="Filter by product category"),
    brand: Optional[str] = Query(None, description="Filter by brand"),
    price_min: Optional[float] = Query(None, description="Minimum price"),
    price_max: Optional[float] = Query(None, description="Maximum price"),
    sort_by: Optional[str] = Query(None, description="Sort by 'price' or 'rating'"),
    order: Optional[str] = Query("asc", description="Sort order: 'asc' or 'desc'")
):
    """
    Return the product catalog with optional filtering and sorting.
    """
    try:
        products = product_service.get_all_products()

        # Apply filtering
        if category:
            products = [p for p in products if p['category'].lower() == category.lower()]
        if brand:
            products = [p for p in products if p['brand'].lower() == brand.lower()]
        if price_min is not None:
            products = [p for p in products if p['price'] >= price_min]
        if price_max is not None:
            products = [p for p in products if p['price'] <= price_max]

        # Apply sorting
        if sort_by in {"price", "rating"}:
            reverse = order == "desc"
            products.sort(key=lambda p: p.get(sort_by, 0), reverse=reverse)

        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve products: {str(e)}")

# Recommendation Endpoint

@app.post("/api/recommendations")
async def get_recommendations(request: RecommendationRequest):
    """
    Generate personalized product recommendations based on user preferences and browsing history.
    """
    try:
        user_preferences = request.preferences.dict()
        browsing_history = request.browsing_history

        recommendations = llm_service.generate_recommendations(
            user_preferences,
            browsing_history,
            product_service.get_all_products()
        )

        return recommendations
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Custom Error Handler

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return {
        "error": str(exc),
        "message": "An error occurred while processing your request"
    }

# Run server

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
