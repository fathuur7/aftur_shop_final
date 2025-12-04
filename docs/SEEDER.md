# 🌱 Panduan Database Seeder

Mengisi database dengan 75 sampel produk.

---

## 🚀 Jalankan Cepat

```bash
.\scripts\seed_auto.bat
```

---

## 📦 Yang Disertakan

### 75 Produk dalam 8 Kategori

| Kategori | Jumlah | Contoh |
|----------|--------|--------|
| Electronics | 15 | Laptop, iPhone, TV, PS5 |
| Fashion | 12 | Sepatu, Tas, Jam Tangan |
| Home & Living | 10 | Sofa, Meja, Lampu |
| Home Appliances | 10 | Air Fryer, Kulkas, AC |
| Books | 8 | Programming, Novel |
| Sports | 10 | Sepeda, Gym Equipment |
| Beauty | 10 | Skincare, Makeup |

### 🖼️ Semua dengan Gambar Unsplash!

Setiap produk menyertakan URL gambar asli:
```
https://images.unsplash.com/photo-xxx?w=400
```

---

## ⚙️ Apa yang Dilakukan

1. **Buat Tabel** - Jika belum ada
2. **Hapus Data** - Menghapus produk yang ada
3. **Masukkan 75 Produk** - Dengan gambar
4. **Tampilkan Ringkasan** - Rincian per kategori

---

## 📊 Output yang Diharapkan

```
============================================================
🌱 AFTUR SHOP DATABASE SEEDER
============================================================

📦 Membuat tabel database...
✅ Tabel berhasil dibuat!

🗑️  Menghapus produk yang ada...
✅ Produk dihapus!

🌱 Seeding 75 sampel produk...
  [01] ✓ Laptop Gaming ASUS ROG Strix
  [02] ✓ iPhone 15 Pro Max 256GB
  ...
  [75] ✓ Catokan Rambut Straightener

✅ Seeded 75/75 produk berhasil!

============================================================
📊 RINGKASAN SEEDING
============================================================
Total Produk    : 75
Total Kategori  : 8

Rincian kategori:
  • Beauty: 10 produk
  • Books: 8 produk
  • Electronics: 15 produk
  • Fashion: 12 produk
  • Home & Living: 10 produk
  • Home Appliances: 10 produk
  • Sports: 10 produk

✅ Seeding database berhasil!
🖼️  Semua produk menyertakan gambar dari Unsplash!
============================================================
```

---

## 🧪 Verifikasi Data

```bash
# Ambil semua produk
curl http://localhost:8000/api/v1/products

# Ambil statistik
curl http://localhost:8000/api/v1/products/stats/all

# Response:
# {"total_products": 75, "total_categories": 8}
```

---

## 🔧 Kustomisasi

Edit `scripts/seed_database.py` untuk menambah produk:

```python
SAMPLE_PRODUCTS = [
    {
        "nama": "Produk Anda",
        "harga": 100000,
        "kategori": "Kategori",
        "gambar": "https://images.unsplash.com/..."
    },
]
```

---

## ⚠️ Catatan

- **Destruktif**: Menghapus semua produk yang ada
- **Idempotent**: Aman dijalankan berkali-kali
- **Gambar**: Hanya URL, tidak diunduh lokal
