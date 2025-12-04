from fastapi import APIRouter

from app.api.v1.endpoints import products, pages

# Create v1 API router
api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(products.router)
api_router.include_router(pages.router)
