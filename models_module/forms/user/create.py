from django.contrib.auth.forms import UserCreationForm

from models_module.models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('avatar', 'email', 'first_name', 'last_name', 'bio', 'password',
                  'is_active', 'is_staff', 'is_superuser',)
