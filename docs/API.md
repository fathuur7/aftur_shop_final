# 🔌 Referensi API

Dokumentasi API lengkap untuk Aftur Shop FastAPI Backend.

**Base URL**: `http://localhost:8000/api/v1`

---

## 📦 API Produk

### Ambil Semua Produk
```http
GET /products
```
**Response**: Array produk dengan id, nama, harga, kategori, gambar

### Ambil Produk berdasarkan ID
```http
GET /products/{id}
```

### Buat Produk Baru
```http
POST /products
Content-Type: multipart/form-data

nama: string (wajib)
harga: float (wajib)
kategori: string (wajib)
gambar: file (opsional)
```

### Update Produk
```http
PUT /products/{id}
Content-Type: multipart/form-data
```

### Hapus Produk
```http
DELETE /products/{id}
```

### Duplikat Produk
```http
POST /products/{id}/duplicate
```
Membuat salinan dengan akhiran "(Copy)".

### Ambil Statistik
```http
GET /products/stats/all
```
Mengembalikan total_products dan total_categories.

---

## 🎭 API Polymorphism

### Format Harga
```http
GET /products/{id}/price
```
**Response**:
```json
{
  "raw_price": 25000000,
  "formatted_price": "Rp 25.000.000"
}
```

### Hitung Diskon
```http
GET /products/{id}/discount/{persen}
```
**Contoh**: `/products/1/discount/20` (diskon 20%)

**Response**:
```json
{
  "original_price": 25000000,
  "discount_percent": 20,
  "final_price": 20000000
}
```

### Ambil Deskripsi
```http
GET /products/{id}/description
```

### Cek Ketersediaan
```http
GET /products/{id}/availability
```

### Demo Polymorphism Lengkap
```http
GET /products/{id}/polymorphism-demo
```
Menampilkan SEMUA 5 method polymorphic dalam satu response.

---

## 📄 API Halaman

### Halaman Utama
```http
GET /pages/home
```

### Kategori
```http
GET /pages/categories
```
Mengelompokkan produk berdasarkan kategori.

### Produk Terlaris
```http
GET /pages/best-sellers
```

### Produk Baru
```http
GET /pages/new-arrivals
```

### Diskon
```http
GET /pages/sale
```

### Kontak
```http
GET /pages/contact
```

### FAQ
```http
GET /pages/faq
```

### Pengiriman
```http
GET /pages/shipping
```

---

## ❤️ Health Check

```http
GET /health
```
**Response**:
```json
{
  "status": "healthy",
  "message": "Aftur Shop API is running"
}
```

---

## 📊 Kode Response

| Kode | Keterangan |
|------|------------|
| 200 | Sukses |
| 201 | Berhasil Dibuat |
| 204 | Tidak Ada Konten (Hapus) |
| 404 | Tidak Ditemukan |
| 422 | Error Validasi |
| 500 | Error Server |

---

## 🧪 Test dengan cURL

```bash
# Ambil semua produk
curl http://localhost:8000/api/v1/products

# Ambil produk 1
curl http://localhost:8000/api/v1/products/1

# Hitung diskon
curl http://localhost:8000/api/v1/products/1/discount/25

# Duplikat produk
curl -X POST http://localhost:8000/api/v1/products/1/duplicate
```

---

**Dokumentasi Interaktif**: http://localhost:8000/docs
