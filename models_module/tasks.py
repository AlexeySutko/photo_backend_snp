from django.utils import timezone

from photo_backend_snp.celery import app

from models_module.models.photo.models import Photo


@app.task
def photo_delayed_deletion():
    photos = Photo.objects.filter(mark_as_deleted_at__lt=timezone.now())
    photos.delete()


@app.task
def test_task(x, y):
    return x + y
