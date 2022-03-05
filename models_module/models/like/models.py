from django.db import models

from models_module.models.photo.models import Photo
from models_module.models.user.models import User


# Junction table
class Like(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE,
                              related_name='likes',
                              related_query_name='like')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='likes',
                             related_query_name='like')
