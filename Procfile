web: python manage.py collectstatic --noinput && gunicorn core.wsgi --log-file -
release: python manage.py migrate && python manage.py force_admin && python manage.py populate_sample_data
