from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from fsm_admin2.admin import FSMTransitionMixin
from models_module.forms.user.change import CustomUserChangeForm
from models_module.forms.user.create import CustomUserCreationForm
from models_module.models.user.models import User

from imagekit.admin import AdminThumbnail


class CustomUserAdmin(FSMTransitionMixin, admin.ModelAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    avatar_display = AdminThumbnail(image_field='avatar',)
    avatar_display.short_description = _('avatar')

    list_display = ('avatar_display', 'email', 'first_name', 'last_name', 'is_active',
                    'is_staff', 'is_superuser', 'last_login')
    list_display_links = ('email',)

    readonly_fields = ['avatar_display', 'auth_token']
