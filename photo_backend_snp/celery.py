import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'photo_backend_snp.settings')

app = Celery('photo_backend_snp')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'delete-marked-photos-every-single-minute': {
        'task': 'models_module.tasks.photo_delayed_deletion',
        'schedule': crontab(),
    },
}
