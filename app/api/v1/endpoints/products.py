from typing import List
from fastapi import APIRouter, Depends, HTTPException, File, UploadFile, Form
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.core.config import settings
from app.models.product import Product
from app.crud.product import ProductRepository
from app.schemas.product import ProductResponse, ProductStats
from app.utils.file_handler import FileHandler

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("", response_model=List[ProductResponse])
def get_all_products(db: Session = Depends(get_db)):
    """
    Get all products from database.
    
    Returns:
        List[ProductResponse]: List of all products
    """
    repo = ProductRepository(db)
    products = repo.get_all()
    return products


@router.get("/{product_id}", response_model=ProductResponse)
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    """
    Get a single product by ID.
    
    Args:
        product_id: ID of the product
        
    Returns:
        ProductResponse: Product data
        
    Raises:
        HTTPException: 404 if product not found
    """
    repo = ProductRepository(db)
    product = repo.get_by_id(product_id)
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return product


@router.post("", response_model=ProductResponse, status_code=201)
async def create_product(
    nama: str = Form(...),
    harga: float = Form(...),
    kategori: str = Form(...),
    gambar: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    """
    Create a new product.
    
    Args:
        nama: Product name
        harga: Product price
        kategori: Product category
        gambar: Product image file (optional)
        
    Returns:
        ProductResponse: Created product
    """
    # Handle file upload using FileHandler utility
    gambar_filename = None
    if gambar:
        file_handler = FileHandler(settings.upload_dir)
        gambar_filename = file_handler.save_upload_file(gambar, prefix=nama)
    
    # Create product object
    product = Product(
        nama=nama,
        harga=harga,
        kategori=kategori,
        gambar=gambar_filename
    )
    
    # Save to database
    repo = ProductRepository(db)
    created_product = repo.create(product)
    
    return created_product


@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: int,
    nama: str = Form(...),
    harga: float = Form(...),
    kategori: str = Form(...),
    gambar: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    """
    Update an existing product.
    
    Args:
        product_id: ID of the product to update
        nama: Product name
        harga: Product price
        kategori: Product category
        gambar: Product image file (optional, only if changing image)
        
    Returns:
        ProductResponse: Updated product
        
    Raises:
        HTTPException: 404 if product not found
    """
    repo = ProductRepository(db)
    existing_product = repo.get_by_id(product_id)
    
    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Handle file upload
    gambar_filename = existing_product.gambar  # Keep existing image by default
    if gambar:
        file_handler = FileHandler(settings.upload_dir)
        
        # Delete old image if exists
        if existing_product.gambar:
            file_handler.delete_file(existing_product.gambar)
        
        # Save new image
        gambar_filename = file_handler.save_upload_file(gambar, prefix=nama)
    
    # Update product
    existing_product.nama = nama
    existing_product.harga = harga
    existing_product.kategori = kategori
    existing_product.gambar = gambar_filename
    
    updated_product = repo.update(existing_product)
    
    return updated_product


@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    """
    Delete a product by ID.
    
    Args:
        product_id: ID of the product to delete
        
    Raises:
        HTTPException: 404 if product not found
    """
    repo = ProductRepository(db)
    success = repo.delete(product_id, settings.upload_dir)
    
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return None


@router.post("/{product_id}/duplicate", response_model=ProductResponse, status_code=201)
def duplicate_product(product_id: int, db: Session = Depends(get_db)):
    """
    Duplicate/clone a product by ID.
    Uses the clone() method from Product class (Polymorphism).
    
    Args:
        product_id: ID of the product to duplicate
        
    Returns:
        ProductResponse: Duplicated product
        
    Raises:
        HTTPException: 404 if product not found
    """
    repo = ProductRepository(db)
    duplicated_product = repo.duplicate(product_id)
    
    if not duplicated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return duplicated_product


@router.get("/stats/all", response_model=ProductStats)
def get_product_stats(db: Session = Depends(get_db)):
    """
    Get product statistics.
    
    Returns:
        ProductStats: Statistics about products
    """
    repo = ProductRepository(db)
    
    return ProductStats(
        total_products=repo.count_products(),
        total_categories=repo.count_categories()
    )


# ==================== POLYMORPHISM DEMONSTRATION ENDPOINTS ====================
# Endpoints di bawah ini mendemonstrasikan penggunaan polymorphic methods

@router.get("/{product_id}/price", response_model=dict)
def get_formatted_price(product_id: int, db: Session = Depends(get_db)):
    """
    Get formatted price display (Polymorphism Demo #2).
    Demonstrates how get_display_price() can be overridden differently.
    
    Args:
        product_id: ID of the product
        
    Returns:
        dict: Formatted price information
        
    Raises:
        HTTPException: 404 if product not found
    """
    repo = ProductRepository(db)
    product = repo.get_by_id(product_id)
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Calls polymorphic method
    formatted_price = product.get_display_price()
    
    return {
        "product_id": product.get_id(),
        "product_name": product.nama,
        "raw_price": product.harga,
        "formatted_price": formatted_price,
        "note": "This uses polymorphic get_display_price() method"
    }


@router.get("/{product_id}/discount/{discount_percent}", response_model=dict)
def calculate_product_discount(
    product_id: int, 
   discount_percent: float, 
    db: Session = Depends(get_db)
):
    """
    Calculate discounted price (Polymorphism Demo #3).
    Demonstrates how calculate_discount() can have different logic per product type.
    
    Args:
        product_id: ID of the product
        discount_percent: Discount percentage (0-100)
        
    Returns:
        dict: Discount calculation details
        
    Raises:
        HTTPException: 404 if product not found
    """
    repo = ProductRepository(db)
    product = repo.get_by_id(product_id)
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Calls polymorphic method
    discounted_price = product.calculate_discount(discount_percent)
    discount_amount = product.harga - discounted_price
    
    return {
        "product_id": product.get_id(),
        "product_name": product.nama,
        "original_price": product.harga,
        "original_formatted": product.get_display_price(),
        "discount_percent": discount_percent,
        "discount_amount": discount_amount,
        "final_price": discounted_price,
        "final_formatted": f"Rp {int(discounted_price):,}".replace(",", "."),
        "note": "This uses polymorphic calculate_discount() method"
    }


@router.get("/{product_id}/description", response_model=dict)
def get_product_description(product_id: int, db: Session = Depends(get_db)):
    """
    Get product description (Polymorphism Demo #4).
    Demonstrates how get_description() format can vary by product type.
    
    Args:
        product_id: ID of the product
        
    Returns:
        dict: Product description
        
    Raises:
        HTTPException: 404 if product not found
    """
    repo = ProductRepository(db)
    product = repo.get_by_id(product_id)
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Calls polymorphic method
    description = product.get_description()
    
    return {
        "product_id": product.get_id(),
        "description": description,
        "note": "This uses polymorphic get_description() method"
    }


@router.get("/{product_id}/availability", response_model=dict)
def check_product_availability(product_id: int, db: Session = Depends(get_db)):
    """
    Check product availability (Polymorphism Demo #5).
    Demonstrates how is_available() logic can differ per product type.
    
    Args:
        product_id: ID of the product
        
    Returns:
        dict: Availability status
        
    Raises:
        HTTPException: 404 if product not found
    """
    repo = ProductRepository(db)
    product = repo.get_by_id(product_id)
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Calls polymorphic method
    is_available = product.is_available()
    
    return {
        "product_id": product.get_id(),
        "product_name": product.nama,
        "is_available": is_available,
        "status": "Available" if is_available else "Not Available",
        "note": "This uses polymorphic is_available() method"
    }


@router.get("/{product_id}/polymorphism-demo", response_model=dict)
def polymorphism_full_demo(product_id: int, db: Session = Depends(get_db)):
    """
    Complete polymorphism demonstration.
    Shows ALL polymorphic methods in action for one product.
    
    Args:
        product_id: ID of the product
        
    Returns:
        dict: All polymorphic method results
        
    Raises:
        HTTPException: 404 if product not found
    """
    repo = ProductRepository(db)
    product = repo.get_by_id(product_id)
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Clone demo
    cloned = product.clone()
    
    return {
        "product_info": {
            "id": product.get_id(),
            "nama": product.nama,
            "harga": product.harga,
            "kategori": product.kategori
        },
        "polymorphism_demonstrations": {
            "1_clone": {
                "method": "clone()",
                "original_name": product.nama,
                "cloned_name": cloned.nama,
                "explanation": "Clone method creates copy with '(Copy)' suffix"
            },
            "2_display_price": {
                "method": "get_display_price()",
                "result": product.get_display_price(),
                "explanation": "Formats price in Rupiah format"
            },
            "3_calculate_discount": {
                "method": "calculate_discount(20)",
                "original": product.harga,
                "discounted_20": product.calculate_discount(20),
                "discounted_50": product.calculate_discount(50),
                "explanation": "Calculates price after discount percentage"
            },
            "4_description": {
                "method": "get_description()",
                "result": product.get_description(),
                "explanation": "Generates detailed product description"
            },
            "5_availability": {
                "method": "is_available()",
                "result": product.is_available(),
                "explanation": "Checks if product is available for purchase"
            }
        },
        "note": "All methods above are POLYMORPHIC - they override abstract methods from ProductPrototype and can be implemented differently by child classes"
    }

