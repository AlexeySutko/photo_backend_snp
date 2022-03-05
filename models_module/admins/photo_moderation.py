from .custom_admin import CustomAdmin
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from fsm_admin2.admin import FSMTransitionMixin
from models_module.forms.photo.moderate import PhotoModerationForm
from models_module.models.photo.models import Photo

from imagekit.admin import AdminThumbnail


def limit_by_state():
    return {'state': 'pending'}


class PhotoModerationAdmin(FSMTransitionMixin, CustomAdmin):

    add_form = PhotoModerationForm
    form = PhotoModerationForm
    model = Photo

    fsm_fields = ['state']

    fsm_transition_form_template = 'fsm_admin2/fsm_transition_form.html'
    fsm_transition_buttons_template = 'fsm_admin2/fsm_transition_buttons.html'

    image_display = AdminThumbnail(image_field='future_image')
    image_display.short_description = _('Future image')

    list_display = ('state', 'owner', 'image_display', 'future_name', 'change_date',)
    list_display_links = ('future_name', 'owner')

    readonly_fields = ['name', 'description']

    def get_queryset(self, request):
        qs = super(PhotoModerationAdmin, self).get_queryset(request)
        qs = qs.filter(Q(state='Pending'))
        return qs
