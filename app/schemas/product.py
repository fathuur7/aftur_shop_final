from pydantic import BaseModel, Field
from typing import Optional


class ProductBase(BaseModel):
    """Base schema untuk Product."""
    nama: str = Field(..., min_length=1, max_length=255, description="Nama produk")
    harga: float = Field(..., gt=0, description="Harga produk (harus lebih dari 0)")
    kategori: str = Field(..., min_length=1, max_length=100, description="Kategori produk")
    gambar: Optional[str] = Field(None, max_length=255, description="Nama file gambar")


class ProductCreate(ProductBase):
    """Schema untuk create product request."""
    pass


class ProductUpdate(ProductBase):
    """Schema untuk update product request."""
    pass


class ProductResponse(ProductBase):
    """Schema untuk product response."""
    id: int = Field(..., description="ID produk")
    
    class Config:
        from_attributes = True  # Pydantic v2 (dulu orm_mode = True)


class ProductStats(BaseModel):
    """Schema untuk product statistics."""
    total_products: int = Field(..., description="Total jumlah produk")
    total_categories: int = Field(..., description="Total kategori unik")
