from models_module.models.user.models import User

from django.db import models

from imagekit.models.fields import ProcessedImageField
from imagekit.processors import ResizeToFill


class Photo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='web_site/static/avatars')
    description = models.TextField()
