from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from models_module.models.user.models import User


# Custom forms to handle Users from Admin
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'bio', 'password',
                  'is_active', 'is_staff', 'is_superuser',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'bio', 'password',
                  'is_active', 'is_staff', 'is_superuser',)