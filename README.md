# 🛒 Aftur Shop - FastAPI Backend

E-commerce backend API dengan **Python FastAPI** dan implementasi OOP concepts.

## ✨ Features

- **Full CRUD** - Create, Read, Update, Delete products
- **OOP Concepts** - Encapsulation, Polymorphism demonstrated
- **75 Sample Products** - 8 categories dengan gambar dari Unsplash
- **API Versioning** - `/api/v1/` prefix
- **Auto Documentation** - Swagger UI built-in

## 🚀 Quick Start

### 1. Setup Environment
```bash
.\scripts\create_venv.bat
```

### 2. Configure Database
Edit `.env` file:
```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=prototype_afturshop
```

### 3. Seed Database
```bash
.\scripts\seed_auto.bat
```

### 4. Run Server
```bash
.\scripts\run_dev.bat
```

**Server:** http://localhost:8000  
**API Docs:** http://localhost:8000/docs

## 📁 Project Structure

```
aftur_shop_final/
├── app/
│   ├── api/v1/endpoints/   # API Routes
│   ├── core/               # Config & Database
│   ├── crud/               # Repository Pattern
│   ├── models/             # SQLAlchemy Models
│   ├── schemas/            # Pydantic Schemas
│   ├── utils/              # Helpers
│   └── main.py             # FastAPI App
├── scripts/                # Batch scripts
├── docs/                   # Documentation
├── uploads/                # Image uploads
└── tests/                  # Unit tests
```

## 🔌 API Endpoints

### Products
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/products` | Get all products |
| GET | `/api/v1/products/{id}` | Get product by ID |
| POST | `/api/v1/products` | Create product |
| PUT | `/api/v1/products/{id}` | Update product |
| DELETE | `/api/v1/products/{id}` | Delete product |
| POST | `/api/v1/products/{id}/duplicate` | Clone product |
| GET | `/api/v1/products/stats/all` | Get statistics |

### Polymorphism Demo
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/products/{id}/price` | Formatted price |
| GET | `/api/v1/products/{id}/discount/{%}` | Calculate discount |
| GET | `/api/v1/products/{id}/description` | Get description |
| GET | `/api/v1/products/{id}/availability` | Check availability |
| GET | `/api/v1/products/{id}/polymorphism-demo` | All methods demo |

### Pages
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/pages/home` | Home page data |
| GET | `/api/v1/pages/categories` | Categories list |
| GET | `/api/v1/pages/best-sellers` | Top products |

## 🎯 OOP Concepts

### Encapsulation
```python
class Product:
    def __init__(self):
        self._id = None  # Private attribute
    
    def get_id(self): return self._id
    def set_id(self, id): self._id = id
```

### Polymorphism
```python
def get_display_price(self) -> str:
    return f"Rp {int(self.harga):,}".replace(",", ".")

def calculate_discount(self, percent: float) -> float:
    return self.harga * (1 - percent/100)
```

## 📦 Sample Data

Seeder includes **75 products** in **8 categories**:
- Electronics (15) - Laptop, iPhone, TV
- Fashion (12) - Shoes, Bags, Watches
- Home & Living (10) - Furniture
- Home Appliances (10) - Kitchen
- Books (8) - Programming, Novels
- Sports (10) - Gym, Outdoor
- Beauty (10) - Skincare, Makeup

All with images from **Unsplash**!

## 📝 Documentation

- [API Reference](docs/API.md)
- [OOP Patterns](docs/OOP.md)
- [Seeder Guide](docs/SEEDER.md)
- [Polymorphism](docs/POLYMORPHISM.md)

## 🛠️ Tech Stack

- **Python 3.13**
- **FastAPI** - Web framework
- **SQLAlchemy** - ORM
- **Pydantic** - Validation
- **MySQL** - Database
- **Uvicorn** - ASGI server

---

Made with ❤️ by Aftur Shop Team
