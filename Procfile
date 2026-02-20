web: python manage.py migrate && python manage.py collectstatic --noinput && python manage.py createinitialadmin && gunicorn core.wsgi --log-file -
release: python manage.py migrate
