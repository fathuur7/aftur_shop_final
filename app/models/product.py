from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base


class Product(Base):
    """
    Product model with OOP concepts demonstration.
    
    Product model dengan SQL Alchemy Base. 
    Class ini mengimplementasikan semua OOP concepts:
    - Encapsulation: Private attribute _id dengan getter/setter
    - Polymorphism: Methods yang bisa di-override oleh child classes
    
    SQLAlchemy mapping ke table 'produk' di database.
    """
    
    __tablename__ = "produk"
    
    # SQLAlchemy columns
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nama = Column(String(255), nullable=False)
    harga = Column(Float, nullable=False)
    kategori = Column(String(100), nullable=False)
    gambar = Column(String(255), nullable=True)
    
    def __init__(self, nama: str, harga: float, kategori: str, gambar: str = None, id: int = None):
        """
        Constructor untuk Product.
        
        Args:
            nama: Nama produk
            harga: Harga produk
            kategori: Kategori produk
            gambar: Nama file gambar produk
            id: ID produk (optional, auto-generated jika tidak disediakan)
        """
        # Initialize attributes
        self.nama = nama
        self.harga = harga
        self.kategori = kategori
        self.gambar = gambar
        
        # (Encapsulation) Private attribute untuk ID
        # Menggunakan underscore untuk menandakan private attribute
        self._id = id
    
    # (Encapsulation) Getter dan Setter untuk private attribute _id
    def set_id(self, id: int) -> None:
        """
        Setter untuk ID produk.
        
        Args:
            id: ID produk
        """
        self._id = id
        self.id = id  # Set SQLAlchemy column juga
    
    def get_id(self) -> int:
        """
        Getter untuk ID produk.
        
        Returns:
            int: ID produk
        """
        return self._id if self._id is not None else self.id
    
    # ==================== POLYMORPHISM METHODS ====================
    # Semua method di bawah ini bisa di-override oleh child classes!
    
    def clone(self) -> 'Product':
        """
        (Polymorphism #1) Clone/duplicate product.
        Membuat copy dari product dengan nama yang ditambahi " (Copy)".
        
        Returns:
            Product: Clone dari product dengan nama yang dimodifikasi
        """
        cloned_product = Product(
            nama=f"{self.nama} (Copy)",
            harga=self.harga,
            kategori=self.kategori,
            gambar=self.gambar
        )
        return cloned_product
    
    def get_display_price(self) -> str:
        """
        (Polymorphism #2) Format harga display.
        Format harga dengan mata uang Rupiah.
        
        Returns:
            str: Formatted price (e.g., "Rp 100.000")
        """
        # Format dengan titik sebagai thousand separator
        formatted = f"{int(self.harga):,}".replace(",", ".")
        return f"Rp {formatted}"
    
    def calculate_discount(self, discount_percent: float) -> float:
        """
        (Polymorphism #3) Calculate discounted price.
        Hitung harga setelah diskon dengan validasi.
        
        Args:
            discount_percent: Persentase diskon (0-100)
            
        Returns:
            float: Harga setelah diskon
        """
        # Validasi discount percent
        if discount_percent < 0:
            discount_percent = 0
        elif discount_percent > 100:
            discount_percent = 100
        
        # Hitung diskon
        discount_amount = self.harga * (discount_percent / 100)
        final_price = self.harga - discount_amount
        
        return round(final_price, 2)
    
    def get_description(self) -> str:
        """
        (Polymorphism #4) Get product description.
        Generate deskripsi produk yang detail.
        
        Returns:
            str: Product description
        """
        return (
            f"{self.nama} - Kategori: {self.kategori}, "
            f"Harga: {self.get_display_price()}"
        )
    
    def is_available(self) -> bool:
        """
        (Polymorphism #5) Check product availability.
        Cek apakah produk tersedia (untuk Product standard, always True).
        
        Returns:
            bool: True (produk tersedia)
        """
        # Untuk standard Product, selalu available
        # Child class bisa override dengan logic berbeda
        # (misal: cek stock, cek status, dll)
        return True
    
    # ==================== END POLYMORPHISM METHODS ====================
    
    def __repr__(self) -> str:
        """String representation untuk debugging."""
        return f"<Product(id={self.get_id()}, nama='{self.nama}', harga={self.harga})>"
