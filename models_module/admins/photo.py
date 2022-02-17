from django.contrib import admin
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from fsm_admin2.admin import FSMTransitionMixin
from models_module.forms.photo.change import PhotoChangeForm
from models_module.forms.photo.create import PhotoCreationForm
from models_module.models.photo.models import Photo

from imagekit.admin import AdminThumbnail


class PhotoAdmin(FSMTransitionMixin, admin.ModelAdmin):

    add_form = PhotoCreationForm
    form = PhotoChangeForm
    model = Photo

    fsm_fields = ['state']

    image_display = AdminThumbnail(image_field='thumbnail',)
    image_display.short_description = _('image')

    readonly_fields = []

    list_display = ('state', 'owner', 'image_display', 'name', 'publish_date', 'mark_as_deleted_at')
    list_display_links = ('name', 'owner')

    def get_queryset(self, request):
        qs = super(PhotoAdmin, self).get_queryset(request)
        qs = qs.filter(Q(state='Approved') | Q(state='New') | Q(state='On deletion'))
        return qs
