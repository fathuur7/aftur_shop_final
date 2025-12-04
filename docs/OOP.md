# 🎯 Pola OOP di Aftur Shop

Implementasi konsep Object-Oriented Programming dalam Python FastAPI.

---

## 1️⃣ Encapsulation (Enkapsulasi)

**Lokasi**: `app/models/product.py`

Atribut private dengan getter/setter:

```python
class Product(Base):
    def __init__(self, nama, harga, kategori, gambar=None, id=None):
        self.nama = nama
        self.harga = harga
        self.kategori = kategori
        self.gambar = gambar
        self._id = id  # Atribut private
    
    # Getter
    def get_id(self) -> int:
        return self._id if self._id else self.id
    
    # Setter
    def set_id(self, id: int):
        self._id = id
        self.id = id
```

**Mengapa?** 
- Mengontrol akses ke data internal
- Validasi sebelum mengatur nilai
- Menyembunyikan detail implementasi

---

## 2️⃣ Polymorphism (Polimorfisme)

**Lokasi**: `app/models/product.py`

5 method yang bisa di-override oleh child class:

### Method 1: clone()
```python
def clone(self) -> 'Product':
    return Product(
        nama=f"{self.nama} (Copy)",
        harga=self.harga,
        kategori=self.kategori,
        gambar=self.gambar
    )
```

### Method 2: get_display_price()
```python
def get_display_price(self) -> str:
    formatted = f"{int(self.harga):,}".replace(",", ".")
    return f"Rp {formatted}"
```

### Method 3: calculate_discount()
```python
def calculate_discount(self, percent: float) -> float:
    if percent < 0: percent = 0
    if percent > 100: percent = 100
    return round(self.harga * (1 - percent/100), 2)
```

### Method 4: get_description()
```python
def get_description(self) -> str:
    return f"{self.nama} - Kategori: {self.kategori}, Harga: {self.get_display_price()}"
```

### Method 5: is_available()
```python
def is_available(self) -> bool:
    return True  # Bisa di-override oleh child class
```

**Mengapa Polymorphism?**
- Nama method sama, perilaku berbeda per class
- Mudah diperluas dengan tipe produk baru
- `DigitalProduct` bisa override `is_available()` dengan cara berbeda

---

## 3️⃣ Repository Pattern

**Lokasi**: `app/crud/product.py`

Mengenkapsulasi operasi database:

```python
class ProductRepository:
    def __init__(self, db: Session):
        self.__db = db  # Session database private
    
    def get_all(self) -> List[Product]:
        return self.__db.query(Product).all()
    
    def get_by_id(self, id: int) -> Optional[Product]:
        return self.__db.query(Product).filter(Product.id == id).first()
    
    def create(self, product: Product) -> Product:
        self.__db.add(product)
        self.__db.commit()
        return product
```

**Manfaat:**
- Single responsibility (tanggung jawab tunggal)
- Mudah untuk test/mock
- Logika database terpisah dari routes

---

## 📊 Ringkasan OOP

| Konsep | Implementasi | File |
|--------|--------------|------|
| Enkapsulasi | Atribut `_id` private | `product.py` |
| Polimorfisme | 5 method yang bisa di-override | `product.py` |
| Repository | Operasi CRUD | `product.py` (crud) |

---

## 🔗 Endpoint API untuk Demo OOP

```bash
# Demo Polymorphism
GET /api/v1/products/1/polymorphism-demo

# Clone (Polymorphism)
POST /api/v1/products/1/duplicate

# Format Harga (Polymorphism)
GET /api/v1/products/1/price
```

Lihat [POLYMORPHISM.md](POLYMORPHISM.md) untuk contoh detail.
