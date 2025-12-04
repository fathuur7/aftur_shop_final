from abc import ABC, abstractmethod


class ProductPrototype(ABC):
    """
    (Abstraction) Penyederhanaan objek, tidak bisa buat product langsung, hanya bisa diturunkan.
    
    Abstract base class untuk Product. Class ini tidak bisa di-instantiate langsung,
    hanya bisa digunakan sebagai parent class.
    
    OOP Concept: ABSTRACTION
    - Menggunakan ABC (Abstract Base Classes) dari Python
    - Mendefinisikan abstract methods yang HARUS diimplementasikan oleh child class
    - Menyediakan template/blueprint untuk Product classes
    """
    
    def __init__(self, nama: str, harga: float, kategori: str, gambar: str):
        """
        Constructor untuk ProductPrototype.
        
        Args:
            nama: Nama produk
            harga: Harga produk
            kategori: Kategori produk
            gambar: Nama file gambar produk
        """
        self.nama = nama
        self.harga = harga
        self.kategori = kategori
        self.gambar = gambar
    
    @abstractmethod
    def clone(self) -> 'ProductPrototype':
        """
        Abstract method untuk cloning/duplicating product.
        Method ini HARUS diimplementasikan oleh child class.
        
        Returns:
            ProductPrototype: Clone dari product
        """
        pass
    
    @abstractmethod
    def get_display_price(self) -> str:
        """
        Abstract method untuk format harga display.
        Setiap child class bisa implement format yang berbeda.
        
        Returns:
            str: Formatted price string
        """
        pass
    
    @abstractmethod
    def calculate_discount(self, discount_percent: float) -> float:
        """
        Abstract method untuk kalkulasi diskon.
        Setiap product type bisa punya aturan diskon berbeda.
        
        Args:
            discount_percent: Persentase diskon (0-100)
            
        Returns:
            float: Harga setelah diskon
        """
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        """
        Abstract method untuk deskripsi produk.
        Setiap product type punya format deskripsi berbeda.
        
        Returns:
            str: Product description
        """
        pass
    
    @abstractmethod
    def is_available(self) -> bool:
        """
        Abstract method untuk cek ketersediaan.
        Bisa berbeda logic untuk tiap product type.
        
        Returns:
            bool: True if available, False otherwise
        """
        pass

