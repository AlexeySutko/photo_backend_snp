from models_module.models.user.models import User
from models_module.managers.photo.manager import CustomPhotoManager
from web_site.services.photo.photo_approve import PhotoApprove
from web_site.services.photo.photo_delete import PhotoDelete

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from django_fsm import FSMField, transition

from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill


STATES = (_('New'), _('Pending'), _('Approved'), _('On deletion'))
STATES = list(zip(STATES, STATES))


class Photo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              verbose_name=_("Author"), related_query_name='photo',
                              related_name='photos')
    name = models.CharField(max_length=50, verbose_name=_("Photo name"))
    image = models.ImageField(upload_to='photos')
    image_size_big = ImageSpecField(autoconvert='image',
                                    source='image',
                                    processors=[ResizeToFill(600, 600)],
                                    format='JPEG',
                                    options={'quality': 100})
    image_size_small = ImageSpecField(autoconvert='image',
                                      source='image',
                                      processors=[ResizeToFill(300, 300)],
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
    change_date = models.DateTimeField(default=timezone.now)
    mark_as_deleted_at = models.DateTimeField(null=True, blank=True, default=None)

    state = FSMField(default='New', choices=STATES)

    objects = CustomPhotoManager

    likes_count = models.IntegerField(default=0)

    class Meta:
        db_table = 'photos'
        verbose_name = _("photo")
        verbose_name_plural = _("photos")

        # Photo state transitions

    @transition(field=state, source=['New', 'Approved', 'On deletion'], target='Pending',
                custom={'short_description': _('Send on moderation')})
    def photo_on_moderation(self):
        pass

    @transition(field=state, source='New', target='Approved',
                custom={'short_description': _('Approve')})
    def photo_approve_new(self):
        pass

    @transition(field=state, source='Pending', target='Approved',
                custom={'short_description': _('Cancel')})
    def photo_cancel_moderation(self):
        PhotoApprove.photo_not_approved(instance=self)

    @transition(field=state, source='Pending', target='Approved',
                custom={'short_description': _('Approve')})
    def photo_approved(self):
        PhotoApprove.photo_update_on_approval(instance=self)

    @transition(field=state, source='Approved', target='On deletion',
                custom={'short_description': _('Send on deletion')})
    def photo_on_deletion(self):
        PhotoDelete.delete_photo(instance=self)

    @transition(field=state, source='On deletion', target='Approved',
                custom={'short_description': _('Cancel deletion')})
    def photo_cancel_deletion(self):
        PhotoDelete.cancel_deletion(instance=self)


# Proxy model to show in admin photos
# that are not approved or on deletion
class ModeratedPhoto(Photo):
    class Meta:
        verbose_name = _("Moderated photo")
        verbose_name_plural = _("Moderated photos")
        proxy = True
