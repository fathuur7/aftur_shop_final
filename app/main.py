from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import os

from app.core.config import settings
from app.core.database import init_db
from app.api.v1.api import api_router

# Initialize FastAPI app
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="FastAPI refactor of Aftur Shop with OOP principles - Best Practices Structure",
    debug=settings.debug,
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files (uploads directory)
if os.path.exists(settings.upload_dir):
    app.mount("/uploads", StaticFiles(directory=settings.upload_dir), name="uploads")
else:
    # Create uploads directory if it doesn't exist
    os.makedirs(settings.upload_dir, exist_ok=True)
    app.mount("/uploads", StaticFiles(directory=settings.upload_dir), name="uploads")

# Include API v1 router
app.include_router(api_router, prefix="/api/v1")


# Exception handlers
@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    """Custom 404 handler."""
    return JSONResponse(
        status_code=404,
        content={"detail": "Resource not found"}
    )


@app.exception_handler(500)
async def internal_error_handler(request: Request, exc):
    """Custom 500 handler."""
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )


# Startup event
@app.on_event("startup")
async def startup_event():
    """
    Startup event handler.
    Initialize database tables if they don't exist.
    """
    print("🚀 Starting Aftur Shop FastAPI...")
    print(f"📦 Database: {settings.db_name}")
    print(f"📁 Upload directory: {settings.upload_dir}")
    print(f"📖 API Docs: http://localhost:8000/docs")
    print(f"🔄 API Version: v1")
    
    # Initialize database (create tables if not exists)
    # Note: In production, use Alembic for migrations
    # init_db()  # Uncomment if you want to auto-create tables


# Root endpoint
@app.get("/")
def root():
    """
    Root endpoint with API information.
    
    Returns:
        Dict: API information
    """
    return {
        "message": "Welcome to Aftur Shop API",
        "version": settings.app_version,
        "docs": "/docs",
        "api_v1": "/api/v1"
    }


@app.get("/health")
def health_check():
    """
    Health check endpoint.
    
    Returns:
        Dict: Application status
    """
    return {
        "status": "healthy",
        "app": settings.app_name,
        "version": settings.app_version
    }


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug
    )
