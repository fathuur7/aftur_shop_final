import os
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.product import Product


class ProductRepository:
    """
    (Encapsulation) Pembungkusan data access logic.
    
    Repository pattern untuk Product data access.
    Class ini meng-encapsulate semua operasi database untuk Product.
    
    OOP Concept: ENCAPSULATION
    - Private attribute _db yang tidak bisa diakses dari luar
    - Semua database operations di-bundle dalam satu class
    - Clean interface untuk CRUD operations
    """
    
    def __init__(self, db: Session):
        """
        Constructor menerima database session.
        
        Args:
            db: SQLAlchemy database session
        """
        # (Encapsulation) Private attribute untuk database session
        self._db = db
    
    def get_all(self) -> List[Product]:
        """
        Mengambil semua data produk dari database.
        
        Returns:
            List[Product]: Array of Product objects
        """
        products = self._db.query(Product).order_by(Product.id.desc()).all()
        
        # Set internal _id for each product
        for product in products:
            product._id = product.id
        
        return products
    
    def count_products(self) -> int:
        """
        Menghitung total jumlah produk.
        
        Returns:
            int: Total jumlah produk
        """
        return self._db.query(func.count(Product.id)).scalar()
    
    def count_categories(self) -> int:
        """
        Menghitung total kategori unik.
        
        Returns:
            int: Total kategori unik
        """
        return self._db.query(func.count(func.distinct(Product.kategori))).scalar()
    
    def get_by_id(self, id: int) -> Optional[Product]:
        """
        Mengambil satu produk berdasarkan ID.
        
        Args:
            id: ID produk
            
        Returns:
            Optional[Product]: Product object atau None jika tidak ditemukan
        """
        product = self._db.query(Product).filter(Product.id == id).first()
        
        if product:
            product._id = product.id
            
        return product
    
    def create(self, product: Product) -> Product:
        """
        Menyimpan produk baru ke database.
        
        Args:
            product: Product object to create
            
        Returns:
            Product: Created product with ID
        """
        self._db.add(product)
        self._db.commit()
        self._db.refresh(product)
        
        product._id = product.id
        
        return product
    
    def update(self, product: Product) -> Product:
        """
        Mengupdate data produk yang sudah ada.
        
        Args:
            product: Product object with updated data
            
        Returns:
            Product: Updated product
        """
        # Get existing product
        existing_product = self.get_by_id(product.get_id())
        
        if existing_product:
            # Update fields
            existing_product.nama = product.nama
            existing_product.harga = product.harga
            existing_product.kategori = product.kategori
            existing_product.gambar = product.gambar
            
            self._db.commit()
            self._db.refresh(existing_product)
            
            existing_product._id = existing_product.id
            
            return existing_product
        
        return None
    
    def delete(self, id: int, upload_dir: str = "uploads") -> bool:
        """
        Menghapus produk berdasarkan ID.
        Juga menghapus file gambar jika ada.
        
        Args:
            id: ID produk yang akan dihapus
            upload_dir: Directory tempat file upload disimpan
            
        Returns:
            bool: True jika berhasil, False jika gagal
        """
        # Get product to delete image file
        product = self.get_by_id(id)
        
        if product:
            # Delete image file if exists
            if product.gambar:
                # Try both paths (from root and from app dir)
                file_paths = [
                    os.path.join(upload_dir, product.gambar),
                    os.path.join("..", upload_dir, product.gambar)
                ]
                
                for file_path in file_paths:
                    if os.path.exists(file_path):
                        try:
                            os.remove(file_path)
                            break
                        except Exception as e:
                            print(f"Error deleting file {file_path}: {e}")
            
            # Delete from database
            self._db.delete(product)
            self._db.commit()
            
            return True
        
        return False
    
    def duplicate(self, id: int) -> Optional[Product]:
        """
        Duplicate/clone produk berdasarkan ID.
        Menggunakan method clone() dari Product (Polymorphism).
        
        Args:
            id: ID produk yang akan diduplikasi
            
        Returns:
            Optional[Product]: Cloned product atau None jika tidak ditemukan
        """
        original_product = self.get_by_id(id)
        
        if original_product:
            # (Polymorphism) Memanggil clone method yang sudah di-override
            cloned_product = original_product.clone()
            
            # Save cloned product to database
            return self.create(cloned_product)
        
        return None
