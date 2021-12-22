from django.db import models
from django.contrib.auth.models import AbstractUser

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# Custom user models for authentication and
# saving additional information about user
class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=4000, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = ProcessedImageField(upload_to='avatars',
                                 processors=[ResizeToFill(100, 100)],
                                 format='JPEG',
                                 options={'quality': 60})

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
