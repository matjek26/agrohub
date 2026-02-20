web: python manage.py migrate && python manage.py collectstatic --noinput && python manage.py createinitialadmin && python manage.py force_admin && python manage.py populate_sample_data && gunicorn core.wsgi --log-file -
release: python manage.py migrate
