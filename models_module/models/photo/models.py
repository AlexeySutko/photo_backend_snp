from models_module.models.user.models import User
from models_module.managers.photo.manager import CustomPhotoManager

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from django_fsm import FSMField

from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit


class Photo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              verbose_name=_("Author"), related_query_name='photo',
                              related_name='photos')
    name = models.CharField(max_length=50, verbose_name=_("Photo name"))
    image = models.ImageField(upload_to='photos')
    image_size_big = ImageSpecField(autoconvert='image',
                                    source='image',
                                    processors=[ResizeToFit(600, 600)],
                                    format='JPEG',
                                    options={'quality': 100})
    image_size_small = ImageSpecField(autoconvert='image',
                                      source='image',
                                      processors=[ResizeToFit(300, 300)],
                                      format='JPEG',
                                      options={'quality': 100})
    thumbnail = ImageSpecField(autoconvert='image',
                               source='image',
                               processors=[ResizeToFit(150, 150)],
                               format='JPEG',
                               options={'quality': 60})
    description = models.TextField(_("Photo description"), blank=True, null=True)
    publish_date = models.DateTimeField(default=timezone.now)

    # Moderation fields
    future_name = models.CharField(max_length=50, verbose_name=_("Future name"), null=True)
    future_description = models.TextField(_("Future description"), blank=True, null=True)
    future_image = models.ImageField(upload_to='photos', verbose_name=_('Future image'), null=True)

    state = FSMField(default='New')

    objects = CustomPhotoManager

    class Meta:
        db_table = 'photos'
        verbose_name = _("photo")
        verbose_name_plural = _("photos")
