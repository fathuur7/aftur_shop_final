# 🎭 Panduan Polymorphism

5 method polymorphic yang didemonstrasikan di API Aftur Shop.

---

## 📚 Apa itu Polymorphism?

**Nama method sama, implementasi berbeda.**

Setiap child class bisa meng-override method dengan cara berbeda. Dalam kasus kita, tipe produk berbeda (Digital, Fisik, Subscription) bisa mengimplementasikan method-method ini dengan logika unik.

---

## 🔥 5 Method Polymorphic

### 1. clone()
Membuat duplikat produk.

```python
def clone(self) -> 'Product':
    return Product(
        nama=f"{self.nama} (Copy)",
        harga=self.harga,
        kategori=self.kategori,
        gambar=self.gambar
    )
```

**API**: `POST /api/v1/products/{id}/duplicate`

---

### 2. get_display_price()
Format harga untuk ditampilkan.

```python
def get_display_price(self) -> str:
    formatted = f"{int(self.harga):,}".replace(",", ".")
    return f"Rp {formatted}"
```

**API**: `GET /api/v1/products/{id}/price`

**Contoh**:
```json
{
  "raw_price": 25000000,
  "formatted_price": "Rp 25.000.000"
}
```

---

### 3. calculate_discount()
Menerapkan persentase diskon.

```python
def calculate_discount(self, percent: float) -> float:
    if percent < 0: percent = 0
    if percent > 100: percent = 100
    return round(self.harga * (1 - percent/100), 2)
```

**API**: `GET /api/v1/products/{id}/discount/{persen}`

**Contoh**: `/products/1/discount/20`
```json
{
  "original_price": 25000000,
  "discount_percent": 20,
  "discount_amount": 5000000,
  "final_price": 20000000
}
```

---

### 4. get_description()
Menghasilkan deskripsi produk.

```python
def get_description(self) -> str:
    return f"{self.nama} - Kategori: {self.kategori}, Harga: {self.get_display_price()}"
```

**API**: `GET /api/v1/products/{id}/description`

---

### 5. is_available()
Mengecek ketersediaan produk.

```python
def is_available(self) -> bool:
    return True  # Override untuk pengecekan stok
```

**API**: `GET /api/v1/products/{id}/availability`

---

## 🌟 Endpoint Demo Lengkap

```http
GET /api/v1/products/{id}/polymorphism-demo
```

Menampilkan SEMUA 5 method dalam satu response:

```json
{
  "product_info": {
    "id": 1,
    "nama": "Laptop Gaming",
    "harga": 25000000
  },
  "polymorphism_demonstrations": {
    "1_clone": {
      "original_name": "Laptop Gaming",
      "cloned_name": "Laptop Gaming (Copy)"
    },
    "2_display_price": {
      "result": "Rp 25.000.000"
    },
    "3_calculate_discount": {
      "discounted_20": 20000000,
      "discounted_50": 12500000
    },
    "4_description": {
      "result": "Laptop Gaming - Kategori: Electronics, Harga: Rp 25.000.000"
    },
    "5_availability": {
      "result": true
    }
  }
}
```

---

## 💡 Mengapa Ini Penting

Child class bisa meng-override dengan cara berbeda:

```python
class DigitalProduct(Product):
    def is_available(self):
        return True  # Selalu tersedia
    
    def calculate_discount(self, percent):
        return super().calculate_discount(min(percent, 50))  # Maksimal diskon 50%

class PhysicalProduct(Product):
    def __init__(self, stock: int, **kwargs):
        super().__init__(**kwargs)
        self.stock = stock
    
    def is_available(self):
        return self.stock > 0  # Cek stok aktual
```

**Pemanggilan method sama, perilaku berbeda!** 🎯
