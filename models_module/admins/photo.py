from django.contrib import admin
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

    fsm_transition_form_template = 'fsm_admin2/fsm_transition_form.html'
    fsm_transition_buttons_template = 'fsm_admin2/fsm_transition_buttons.html'

    image_display = AdminThumbnail(image_field='thumbnail',)
    image_display.short_description = _('image')

    readonly_fields = ()

    list_display = ('owner', 'image_display', 'name', 'publish_date',)
    list_display_links = ('name', 'owner')
