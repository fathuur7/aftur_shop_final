@echo off
echo Starting Aftur Shop FastAPI Development Server...
echo.

REM Check if venv exists
if not exist venv (
    echo ERROR: Virtual environment not found!
    echo Please run scripts\create_venv.bat first to create the virtual environment.
    echo.
    pause
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Check if activation was successful
if %errorlevel% neq 0 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)

echo Virtual environment activated
echo.
echo ========================================
echo Starting FastAPI server...
echo ========================================
echo Server will be available at: http://localhost:8000
echo API documentation at: http://localhost:8000/docs
echo API v1: http://localhost:8000/api/v1
echo ========================================
echo.

REM Run FastAPI development server with new main location
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

REM If server stops, deactivate venv
deactivate
