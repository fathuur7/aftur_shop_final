@echo off
echo ========================================
echo 🌱 Database Seeder - Aftur Shop
echo ========================================
echo.

REM Check if venv exists
if not exist venv (
    echo ERROR: Virtual environment not found!
    echo Please run scripts\create_venv.bat first.
    echo.
    pause
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate.bat

echo Running database seeder...
echo This will:
echo   1. Create tables if not exist
echo   2. Clear existing products
echo   3. Insert sample products
echo.
echo ========================================
echo Starting seeder...
echo ========================================
echo.

REM Run seeder script WITHOUT confirmation
python scripts\seed_database.py

echo.
echo ========================================
echo.

REM Check if successful
if %errorlevel% equ 0 (
    echo ✅ Seeding completed successfully!
    echo.
    echo You can now:
    echo   1. Run the server: .\scripts\run_dev.bat
    echo   2. Check API docs: http://localhost:8000/docs
    echo   3. View products: http://localhost:8000/api/v1/products
) else (
    echo ❌ Seeding failed! Check the error messages above.
)

echo.
pause

REM Deactivate venv
deactivate
