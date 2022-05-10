from django.db import models


class PhotoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().prefetch_related('likes').select_related('owner')
