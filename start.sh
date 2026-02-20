#!/bin/bash
# Railway startup script

echo "Running migrations..."
python manage.py migrate --noinput

echo "Running first-time setup..."
python manage.py setup_once

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
exec gunicorn core.wsgi --bind 0.0.0.0:$PORT --log-file -
