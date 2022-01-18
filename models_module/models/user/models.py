from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from models_module.managers.user.manager import CustomUserManager


# Custom user models for authentication and
# saving additional information about user
class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    bio = models.TextField(_("bio"), max_length=4000, blank=True)
    birth_date = models.DateField(_('date of birth'), null=True, blank=True)
    avatar = ProcessedImageField(upload_to='web_site/static/avatars',
                                 processors=[ResizeToFill(100, 100)],
                                 format='JPEG',
                                 options={'quality': 60})

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        db_table = 'users'
        verbose_name = _("user")
        verbose_name_plural = _("users")
