from django.contrib import admin
from models_module.forms.user.custom_change import CustomUserChangeForm
from models_module.forms.user.custom_creation import CustomUserCreationForm
from models_module.models.user.models import User


class CustomUserAdmin(admin.ModelAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    list_display = ('email', 'first_name', 'last_name', 'is_active',
                    'is_staff', 'is_superuser', 'last_login',)
    list_display_links = ('email',)
