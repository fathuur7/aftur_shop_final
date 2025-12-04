# ⚡ Quick Start Guide

## Prerequisites
- Python 3.10+
- MySQL Server
- Git (optional)

## 🚀 4 Steps to Run

### Step 1: Setup Virtual Environment
```bash
cd c:\Users\kopis\Documents\aftur_shop_final
.\scripts\create_venv.bat
```
Wait until all dependencies installed.

### Step 2: Configure Database
Edit `.env` file if needed:
```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=
DB_NAME=prototype_afturshop
```

### Step 3: Seed Database
```bash
.\scripts\seed_auto.bat
```
This creates **75 sample products** with images!

### Step 4: Run Server
```bash
.\scripts\run_dev.bat
```

## ✅ Done!

- **Server**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Products**: http://localhost:8000/api/v1/products

## 🧪 Quick Test

```bash
# Get all products
curl http://localhost:8000/api/v1/products

# Test polymorphism
curl http://localhost:8000/api/v1/products/1/polymorphism-demo

# Get stats
curl http://localhost:8000/api/v1/products/stats/all
```

## 📦 What's Included

After seeding:
- **75 products** across **8 categories**
- All products have **Unsplash images**
- Ready to test all API endpoints

## 🔧 Troubleshooting

### "Module not found" error
```bash
pip install -r requirements.txt
```

### Database connection failed
1. Check MySQL is running
2. Verify `.env` credentials
3. Create database: `CREATE DATABASE prototype_afturshop`

### Port 8000 already in use
Kill existing process or change port in `run_dev.bat`

---

Need help? Check [README.md](README.md) or [docs/](docs/) folder.
