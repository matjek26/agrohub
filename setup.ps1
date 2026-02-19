# Agrohub Quick Start Script
# Run this script to set up the database and create initial data

Write-Host "========================================" -ForegroundColor Green
Write-Host "   AGROHUB SETUP SCRIPT" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

# Check if virtual environment is activated
if (-not $env:VIRTUAL_ENV) {
    Write-Host "Virtual environment not detected. Activating..." -ForegroundColor Yellow
    .\venv\Scripts\Activate.ps1
}

Write-Host "[1/5] Creating database migrations..." -ForegroundColor Cyan
python manage.py makemigrations

Write-Host "[2/5] Applying migrations..." -ForegroundColor Cyan
python manage.py migrate

Write-Host "[3/5] Creating categories..." -ForegroundColor Cyan
python manage.py shell -c @"
from marketplace.models import Category

categories = [
    {'name': 'aquaculture', 'display_name': 'Aquaculture', 'description': 'Fish farming and aquatic products', 'order': 1},
    {'name': 'seafoods', 'display_name': 'Seafoods', 'description': 'Fresh seafood products', 'order': 2},
    {'name': 'agro_processed', 'display_name': 'Agro-Processed', 'description': 'Processed agricultural goods', 'order': 3},
    {'name': 'courses', 'display_name': 'Courses Offered', 'description': 'Agricultural training and courses', 'order': 4},
    {'name': 'tools_rent', 'display_name': 'Tools for Rent', 'description': 'Agricultural equipment rental', 'order': 5},
    {'name': 'jobs', 'display_name': 'Jobs in Agro', 'description': 'Career opportunities in agriculture', 'order': 6},
]

for cat in categories:
    obj, created = Category.objects.get_or_create(name=cat['name'], defaults=cat)
    if created:
        print(f'Created category: {cat[\"display_name\"]}')
    else:
        print(f'Category already exists: {cat[\"display_name\"]}')
"@

Write-Host "[4/5] Creating superuser account..." -ForegroundColor Cyan
Write-Host "Please enter superuser details:" -ForegroundColor Yellow
python manage.py createsuperuser

Write-Host "[5/5] Collecting static files..." -ForegroundColor Cyan
python manage.py collectstatic --noinput

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "   SETUP COMPLETE!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "To start the development server, run:" -ForegroundColor Cyan
Write-Host "  python manage.py runserver" -ForegroundColor White
Write-Host ""
Write-Host "Then open your browser to:" -ForegroundColor Cyan
Write-Host "  http://localhost:8000" -ForegroundColor White
Write-Host ""
Write-Host "Admin panel:" -ForegroundColor Cyan
Write-Host "  http://localhost:8000/admin" -ForegroundColor White
Write-Host ""
Write-Host "Happy selling! 🌾" -ForegroundColor Green
