import os

from celery import Celery
from decouple import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")

app = Celery("main", backend=config("REDIS_URL"), broker=config("REDIS_URL"))

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
