web: celery -A main worker --loglevel=info & python manage.py migrate && gunicorn main.wsgi  --bind 0.0.0.0:$PORT


