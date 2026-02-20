#!/bin/bash
# Railway startup script

echo "Running migrations..."
python manage.py migrate --noinput

echo "Creating admin user..."
python manage.py force_admin || echo "Admin already exists"

echo "Loading sample data..."
python manage.py populate_sample_data || echo "Sample data already loaded"

echo "Starting Gunicorn..."
gunicorn core.wsgi --bind 0.0.0.0:$PORT --log-file -
