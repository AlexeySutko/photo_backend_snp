from django.contrib import admin
from .user_forms import CustomUserChangeForm, CustomUserCreationForm
from models_module.models.user.models import User


class CustomUserAdmin(admin.ModelAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    list_display = ('email', 'first_name', 'last_name', 'is_active',
                    'is_staff', 'is_superuser', 'last_login',)
    list_display_links = ('email',)
