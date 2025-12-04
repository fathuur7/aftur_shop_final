from typing import Dict, Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.crud.product import ProductRepository

router = APIRouter(prefix="/pages", tags=["Pages"])


@router.get("/home")
def home(db: Session = Depends(get_db)) -> Dict[str, Any]:
    """
    Home page data.
    
    Returns:
        Dict: Home page information with products
    """
    repo = ProductRepository(db)
    products = repo.get_all()
    
    return {
        "page": "home",
        "title": "Aftur Shop - Home",
        "total_products": repo.count_products(),
        "total_categories": repo.count_categories(),
        "products": products
    }


@router.get("/best-sellers")
def best_sellers(db: Session = Depends(get_db)) -> Dict[str, Any]:
    """
    Best sellers page data.
    
    Returns:
        Dict: Best sellers information
    """
    repo = ProductRepository(db)
    products = repo.get_all()
    
    return {
        "page": "best_sellers",
        "title": "Best Sellers - Aftur Shop",
        "products": products[:10]  # Top 10 products
    }


@router.get("/new-arrivals")
def new_arrivals(db: Session = Depends(get_db)) -> Dict[str, Any]:
    """
    New arrivals page data.
    
    Returns:
        Dict: New arrivals information
    """
    repo = ProductRepository(db)
    products = repo.get_all()
    
    return {
        "page": "new_arrivals",
        "title": "New Arrivals - Aftur Shop",
        "products": products[:10]  # Latest 10 products
    }


@router.get("/categories")
def categories(db: Session = Depends(get_db)) -> Dict[str, Any]:
    """
    Categories page data.
    Groups products by category.
    
    Returns:
        Dict: Categories information
    """
    repo = ProductRepository(db)
    products = repo.get_all()
    
    # Group products by category
    categories_dict = {}
    for product in products:
        if product.kategori not in categories_dict:
            categories_dict[product.kategori] = []
        categories_dict[product.kategori].append(product)
    
    return {
        "page": "categories",
        "title": "Categories - Aftur Shop",
        "categories": categories_dict,
        "total_categories": len(categories_dict)
    }


@router.get("/sale")
def sale(db: Session = Depends(get_db)) -> Dict[str, Any]:
    """
    Sale page data.
    
    Returns:
        Dict: Sale information
    """
    repo = ProductRepository(db)
    products = repo.get_all()
    
    return {
        "page": "sale",
        "title": "Sale - Aftur Shop",
        "products": products
    }


@router.get("/contact")
def contact() -> Dict[str, Any]:
    """
    Contact page data.
    
    Returns:
        Dict: Contact information
    """
    return {
        "page": "contact",
        "title": "Contact Us - Aftur Shop",
        "email": "contact@afturshop.com",
        "phone": "+62 123 456 7890",
        "address": "Jakarta, Indonesia"
    }


@router.get("/faq")
def faq() -> Dict[str, Any]:
    """
    FAQ page data.
    
    Returns:
        Dict: FAQ information
    """
    return {
        "page": "faq",
        "title": "FAQ - Aftur Shop",
        "faqs": [
            {
                "question": "How do I place an order?",
                "answer": "You can browse our products and add items to your cart."
            },
            {
                "question": "What payment methods do you accept?",
                "answer": "We accept various payment methods including credit cards and bank transfers."
            },
            {
                "question": "How long is shipping?",
                "answer": "Shipping typically takes 3-5 business days."
            }
        ]
    }


@router.get("/shipping")
def shipping() -> Dict[str, Any]:
    """
    Shipping & Returns page data.
    
    Returns:
        Dict: Shipping information
    """
    return {
        "page": "shipping",
        "title": "Shipping & Returns - Aftur Shop",
        "shipping_info": "We offer free shipping on orders over $50.",
        "returns_info": "Returns accepted within 30 days of purchase."
    }
