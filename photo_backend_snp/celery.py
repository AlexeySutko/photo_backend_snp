import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'photo_backend_snp.settings')

app = Celery('photo_backend_snp')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()