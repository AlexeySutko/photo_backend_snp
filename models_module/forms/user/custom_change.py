from django.contrib.auth.forms import UserChangeForm

from models_module.models import User


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'bio', 'password',
                  'is_active', 'is_staff', 'is_superuser',)