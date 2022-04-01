from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from models_module.models.photo.models import Photo
from models_module.models.user.models import User


# Junction table
class Like(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE,
                              related_name='likes',
                              related_query_name='likes')

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='likes',
                             related_query_name='likes')

    class Meta:
        db_table = 'likes'
        verbose_name = "like"
        verbose_name_plural = "likes"
