@echo off
echo ========================================
echo    AGROHUB QUICK START
echo ========================================
echo.

echo [1/4] Activating virtual environment...
call venv\Scripts\activate.bat

echo [2/4] Installing dependencies...
pip install -r requirements.txt

echo [3/4] Setting up database...
python manage.py makemigrations
python manage.py migrate

echo [4/4] Running sample data population...
python manage.py populate_sample_data

echo.
echo ========================================
echo    SETUP COMPLETE!
echo ========================================
echo.
echo To start the server, run:
echo   python manage.py runserver
echo.
echo Then open: http://localhost:8000
echo.
pause
