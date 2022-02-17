from photo_backend_snp import celery_app
from django.utils import timezone
import datetime


class PhotoDelete:

    @staticmethod
    def delete_photo(instance):
        from models_module.models.photo.models import Photo
        if instance.__class__ is Photo:
            photo = instance
            photo.mark_as_deleted_at = timezone.now() + datetime.timedelta(seconds=120)

    @staticmethod
    def cancel_deletion(instance):
        photo = instance
        photo.mark_as_deleted_at = None

