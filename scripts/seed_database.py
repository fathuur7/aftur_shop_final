"""
Database Seeder for Aftur Shop
Populate database with sample product data including images from internet
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from app.core.database import SessionLocal, engine, Base
from app.models.product import Product
from app.crud.product import ProductRepository


# Sample products data with internet images
SAMPLE_PRODUCTS = [
    # ==================== ELECTRONICS (15 products) ====================
    {
        "nama": "Laptop Gaming ASUS ROG Strix",
        "harga": 25000000,
        "kategori": "Electronics",
        "gambar": "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=400"
    },
    {
        "nama": "iPhone 15 Pro Max 256GB",
        "harga": 22000000,
        "kategori": "Electronics",
        "gambar": "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?w=400"
    },
    {
        "nama": "Samsung Galaxy S24 Ultra",
        "harga": 19000000,
        "kategori": "Electronics",
        "gambar": "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=400"
    },
    {
        "nama": "MacBook Pro M3 14 inch",
        "harga": 35000000,
        "kategori": "Electronics",
        "gambar": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400"
    },
    {
        "nama": "Sony WH-1000XM5 Headphones",
        "harga": 5500000,
        "kategori": "Electronics",
        "gambar": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400"
    },
    {
        "nama": "iPad Air M2 256GB",
        "harga": 12000000,
        "kategori": "Electronics",
        "gambar": "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=400"
    },
    {
        "nama": "Sony PlayStation 5",
        "harga": 8500000,
        "kategori": "Electronics",
        "gambar": "https://images.unsplash.com/photo-1606144042614-b2417e99c4e3?w=400"
    },
    {
        "nama": "Nintendo Switch OLED",
        "harga": 5200000,
        "kategori": "Electronics",
        "gambar": "https://images.unsplash.com/photo-1578303512597-81e6cc155b3e?w=400"
    },
    {
        "nama": "Canon EOS R6 Mark II",
        "harga": 42000000,
        "kategori": "Electronics",
        "gambar": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=400"
    },
    {
        "nama": "GoPro Hero 12 Black",
        "harga": 6800000,
        "kategori": "Electronics",
        "gambar": "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=400"
    },
    {
        "nama": "Samsung 65 inch QLED TV",
        "harga": 18000000,
        "kategori": "Electronics",
        "gambar": "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400"
    },
    {
        "nama": "Apple Watch Ultra 2",
        "harga": 14500000,
        "kategori": "Electronics",
        "gambar": "https://images.unsplash.com/photo-1434493789847-2f02dc6ca35d?w=400"
    },
    {
        "nama": "JBL Flip 6 Speaker",
        "harga": 1800000,
        "kategori": "Electronics",
        "gambar": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=400"
    },
    {
        "nama": "Logitech MX Master 3S Mouse",
        "harga": 1500000,
        "kategori": "Electronics",
        "gambar": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=400"
    },
    {
        "nama": "Mechanical Keyboard RGB",
        "harga": 1200000,
        "kategori": "Electronics",
        "gambar": "https://images.unsplash.com/photo-1511467687858-23d96c32e4ae?w=400"
    },
    
    # ==================== FASHION (12 products) ====================
    {
        "nama": "Kemeja Batik Premium Solo",
        "harga": 450000,
        "kategori": "Fashion",
        "gambar": "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=400"
    },
    {
        "nama": "Nike Air Max 270",
        "harga": 2500000,
        "kategori": "Fashion",
        "gambar": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400"
    },
    {
        "nama": "Adidas Ultraboost 23",
        "harga": 2800000,
        "kategori": "Fashion",
        "gambar": "https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=400"
    },
    {
        "nama": "Tas Kulit Branded Premium",
        "harga": 1800000,
        "kategori": "Fashion",
        "gambar": "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=400"
    },
    {
        "nama": "Jam Tangan Casio G-Shock",
        "harga": 2200000,
        "kategori": "Fashion",
        "gambar": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400"
    },
    {
        "nama": "Kacamata Rayban Aviator",
        "harga": 3200000,
        "kategori": "Fashion",
        "gambar": "https://images.unsplash.com/photo-1572635196237-14b3f281503f?w=400"
    },
    {
        "nama": "Jaket Denim Vintage",
        "harga": 650000,
        "kategori": "Fashion",
        "gambar": "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400"
    },
    {
        "nama": "Hoodie Premium Cotton",
        "harga": 350000,
        "kategori": "Fashion",
        "gambar": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=400"
    },
    {
        "nama": "Celana Jeans Slim Fit",
        "harga": 450000,
        "kategori": "Fashion",
        "gambar": "https://images.unsplash.com/photo-1542272604-787c3835535d?w=400"
    },
    {
        "nama": "Topi Baseball NY Cap",
        "harga": 250000,
        "kategori": "Fashion",
        "gambar": "https://images.unsplash.com/photo-1588850561407-ed78c282e89b?w=400"
    },
    {
        "nama": "Dompet Kulit Asli",
        "harga": 380000,
        "kategori": "Fashion",
        "gambar": "https://images.unsplash.com/photo-1627123424574-724758594e93?w=400"
    },
    {
        "nama": "Sabuk Kulit Premium",
        "harga": 280000,
        "kategori": "Fashion",
        "gambar": "https://images.unsplash.com/photo-1624222247344-550fb60583dc?w=400"
    },
    
    # ==================== HOME & LIVING (10 products) ====================
    {
        "nama": "Sofa Minimalis 3 Seater",
        "harga": 8500000,
        "kategori": "Home & Living",
        "gambar": "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=400"
    },
    {
        "nama": "Meja Makan Kayu Jati",
        "harga": 6500000,
        "kategori": "Home & Living",
        "gambar": "https://images.unsplash.com/photo-1617806118233-18e1de247200?w=400"
    },
    {
        "nama": "Lemari Pakaian Sliding 3 Pintu",
        "harga": 7500000,
        "kategori": "Home & Living",
        "gambar": "https://images.unsplash.com/photo-1558997519-83ea9252edf8?w=400"
    },
    {
        "nama": "Kasur Spring Bed King Size",
        "harga": 9500000,
        "kategori": "Home & Living",
        "gambar": "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=400"
    },
    {
        "nama": "Rak Buku Minimalis",
        "harga": 1200000,
        "kategori": "Home & Living",
        "gambar": "https://images.unsplash.com/photo-1594620302200-9a762244a156?w=400"
    },
    {
        "nama": "Lampu Gantung Modern",
        "harga": 850000,
        "kategori": "Home & Living",
        "gambar": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=400"
    },
    {
        "nama": "Karpet Turki Premium",
        "harga": 2500000,
        "kategori": "Home & Living",
        "gambar": "https://images.unsplash.com/photo-1600166898405-da9535204843?w=400"
    },
    {
        "nama": "Cermin Dinding Aesthetic",
        "harga": 450000,
        "kategori": "Home & Living",
        "gambar": "https://images.unsplash.com/photo-1618220179428-22790b461013?w=400"
    },
    {
        "nama": "Vas Bunga Keramik Set",
        "harga": 350000,
        "kategori": "Home & Living",
        "gambar": "https://images.unsplash.com/photo-1578500494198-246f612d3b3d?w=400"
    },
    {
        "nama": "Tanaman Hias Monstera",
        "harga": 180000,
        "kategori": "Home & Living",
        "gambar": "https://images.unsplash.com/photo-1614594975525-e45c9c56d1e7?w=400"
    },
    
    # ==================== HOME APPLIANCES (10 products) ====================
    {
        "nama": "Air Fryer Philips 4.1L",
        "harga": 2200000,
        "kategori": "Home Appliances",
        "gambar": "https://images.unsplash.com/photo-1626509653291-18d9a934b9db?w=400"
    },
    {
        "nama": "Rice Cooker Digital 1.8L",
        "harga": 950000,
        "kategori": "Home Appliances",
        "gambar": "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=400"
    },
    {
        "nama": "Blender Philips 2in1",
        "harga": 750000,
        "kategori": "Home Appliances",
        "gambar": "https://images.unsplash.com/photo-1570222094114-d054a817e56b?w=400"
    },
    {
        "nama": "Vacuum Cleaner Robot Xiaomi",
        "harga": 4500000,
        "kategori": "Home Appliances",
        "gambar": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400"
    },
    {
        "nama": "Microwave Oven Samsung",
        "harga": 1800000,
        "kategori": "Home Appliances",
        "gambar": "https://images.unsplash.com/photo-1574269909862-7e1d70bb8078?w=400"
    },
    {
        "nama": "Mesin Cuci Front Load LG",
        "harga": 7500000,
        "kategori": "Home Appliances",
        "gambar": "https://images.unsplash.com/photo-1626806787461-102c1bfaaea1?w=400"
    },
    {
        "nama": "AC Daikin 1 PK Inverter",
        "harga": 5800000,
        "kategori": "Home Appliances",
        "gambar": "https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=400"
    },
    {
        "nama": "Kulkas 2 Pintu Samsung",
        "harga": 8500000,
        "kategori": "Home Appliances",
        "gambar": "https://images.unsplash.com/photo-1571175443880-49e1d25b2bc5?w=400"
    },
    {
        "nama": "Dispenser Hot Cold Miyako",
        "harga": 650000,
        "kategori": "Home Appliances",
        "gambar": "https://images.unsplash.com/photo-1548839140-29a749e1cf4d?w=400"
    },
    {
        "nama": "Setrika Uap Philips",
        "harga": 450000,
        "kategori": "Home Appliances",
        "gambar": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400"
    },
    
    # ==================== BOOKS (8 products) ====================
    {
        "nama": "Buku Python Programming",
        "harga": 185000,
        "kategori": "Books",
        "gambar": "https://images.unsplash.com/photo-1532012197267-da84d127e765?w=400"
    },
    {
        "nama": "Novel Laskar Pelangi",
        "harga": 95000,
        "kategori": "Books",
        "gambar": "https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=400"
    },
    {
        "nama": "Buku Rich Dad Poor Dad",
        "harga": 125000,
        "kategori": "Books",
        "gambar": "https://images.unsplash.com/photo-1512820790803-83ca734da794?w=400"
    },
    {
        "nama": "Buku Atomic Habits",
        "harga": 135000,
        "kategori": "Books",
        "gambar": "https://images.unsplash.com/photo-1589998059171-988d887df646?w=400"
    },
    {
        "nama": "Kamus Bahasa Inggris Lengkap",
        "harga": 175000,
        "kategori": "Books",
        "gambar": "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=400"
    },
    {
        "nama": "Buku The Psychology of Money",
        "harga": 145000,
        "kategori": "Books",
        "gambar": "https://images.unsplash.com/photo-1543002588-bfa74002ed7e?w=400"
    },
    {
        "nama": "Buku Clean Code",
        "harga": 225000,
        "kategori": "Books",
        "gambar": "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=400"
    },
    {
        "nama": "Komik One Piece Vol 1-10",
        "harga": 350000,
        "kategori": "Books",
        "gambar": "https://images.unsplash.com/photo-1618519764620-7403abdbdfe9?w=400"
    },
    
    # ==================== SPORTS (10 products) ====================
    {
        "nama": "Sepeda MTB Pacific",
        "harga": 3500000,
        "kategori": "Sports",
        "gambar": "https://images.unsplash.com/photo-1532298229144-0ec0c57515c7?w=400"
    },
    {
        "nama": "Raket Badminton Yonex",
        "harga": 850000,
        "kategori": "Sports",
        "gambar": "https://images.unsplash.com/photo-1617083934551-ac1f1c559c64?w=400"
    },
    {
        "nama": "Bola Sepak Nike Strike",
        "harga": 450000,
        "kategori": "Sports",
        "gambar": "https://images.unsplash.com/photo-1614632537423-1e6c2e7e0aab?w=400"
    },
    {
        "nama": "Matras Yoga Premium",
        "harga": 350000,
        "kategori": "Sports",
        "gambar": "https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?w=400"
    },
    {
        "nama": "Dumbbell Set 20kg",
        "harga": 750000,
        "kategori": "Sports",
        "gambar": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400"
    },
    {
        "nama": "Treadmill Elektrik Speeds",
        "harga": 5500000,
        "kategori": "Sports",
        "gambar": "https://images.unsplash.com/photo-1576678927484-cc907957088c?w=400"
    },
    {
        "nama": "Sepatu Futsal Specs",
        "harga": 650000,
        "kategori": "Sports",
        "gambar": "https://images.unsplash.com/photo-1579338559194-a162d19bf842?w=400"
    },
    {
        "nama": "Jersey Timnas Indonesia",
        "harga": 450000,
        "kategori": "Sports",
        "gambar": "https://images.unsplash.com/photo-1580087433295-ab2600c1030e?w=400"
    },
    {
        "nama": "Tas Olahraga Nike Gym",
        "harga": 550000,
        "kategori": "Sports",
        "gambar": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=400"
    },
    {
        "nama": "Botol Minum Tumbler 1L",
        "harga": 185000,
        "kategori": "Sports",
        "gambar": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=400"
    },
    
    # ==================== BEAUTY (10 products) ====================
    {
        "nama": "Skincare Set Wardah",
        "harga": 350000,
        "kategori": "Beauty",
        "gambar": "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=400"
    },
    {
        "nama": "Parfum Jo Malone 100ml",
        "harga": 2500000,
        "kategori": "Beauty",
        "gambar": "https://images.unsplash.com/photo-1541643600914-78b084683601?w=400"
    },
    {
        "nama": "Makeup Palette NYX",
        "harga": 450000,
        "kategori": "Beauty",
        "gambar": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=400"
    },
    {
        "nama": "Lipstick Maybelline Set",
        "harga": 280000,
        "kategori": "Beauty",
        "gambar": "https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=400"
    },
    {
        "nama": "Hair Dryer Philips 2100W",
        "harga": 650000,
        "kategori": "Beauty",
        "gambar": "https://images.unsplash.com/photo-1522338140262-f46f5913618a?w=400"
    },
    {
        "nama": "Sunscreen SPF 50 Skin Aqua",
        "harga": 125000,
        "kategori": "Beauty",
        "gambar": "https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=400"
    },
    {
        "nama": "Face Serum Vitamin C",
        "harga": 185000,
        "kategori": "Beauty",
        "gambar": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=400"
    },
    {
        "nama": "Brush Makeup Set 12pcs",
        "harga": 250000,
        "kategori": "Beauty",
        "gambar": "https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=400"
    },
    {
        "nama": "Masker Wajah Premium",
        "harga": 85000,
        "kategori": "Beauty",
        "gambar": "https://images.unsplash.com/photo-1596755389378-c31d21fd1273?w=400"
    },
    {
        "nama": "Catokan Rambut Straightener",
        "harga": 450000,
        "kategori": "Beauty",
        "gambar": "https://images.unsplash.com/photo-1527799820374-dcf8d9d4a388?w=400"
    },
]


def create_tables():
    """Create all database tables."""
    print("📦 Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created successfully!")


def clear_products(db: SessionLocal):
    """Clear all existing products."""
    print("🗑️  Clearing existing products...")
    db.query(Product).delete()
    db.commit()
    print("✅ Products cleared!")


def seed_products(db: SessionLocal):
    """Seed sample products into database."""
    print(f"🌱 Seeding {len(SAMPLE_PRODUCTS)} sample products...")
    
    repo = ProductRepository(db)
    created_count = 0
    
    for i, product_data in enumerate(SAMPLE_PRODUCTS, 1):
        try:
            product = Product(**product_data)
            repo.create(product)
            created_count += 1
            print(f"  [{i:02d}] ✓ {product_data['nama'][:40]}")
        except Exception as e:
            print(f"  [{i:02d}] ✗ {product_data['nama'][:40]}: {e}")
    
    print(f"\n✅ Seeded {created_count}/{len(SAMPLE_PRODUCTS)} products successfully!")


def main():
    """Main seeder function."""
    print("=" * 60)
    print("🌱 AFTUR SHOP DATABASE SEEDER")
    print("   With images from Unsplash!")
    print("=" * 60)
    print()
    
    # Create tables if not exist
    create_tables()
    print()
    
    # Create database session
    db = SessionLocal()
    
    try:
        # Clear existing data
        clear_products(db)
        print()
        
        # Seed sample products
        seed_products(db)
        print()
        
        # Verify seeded data
        repo = ProductRepository(db)
        total = repo.count_products()
        categories = repo.count_categories()
        
        print("=" * 60)
        print("📊 SEEDING SUMMARY")
        print("=" * 60)
        print(f"Total Products : {total}")
        print(f"Total Categories: {categories}")
        print()
        print("Categories breakdown:")
        products = repo.get_all()
        cat_count = {}
        for p in products:
            cat_count[p.kategori] = cat_count.get(p.kategori, 0) + 1
        for cat, count in sorted(cat_count.items()):
            print(f"  • {cat}: {count} products")
        print()
        print("✅ Database seeding completed successfully!")
        print("🖼️  All products include images from Unsplash!")
        print("=" * 60)
        
    except Exception as e:
        print(f"❌ Error during seeding: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    main()
