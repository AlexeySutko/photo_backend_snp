from models_module.models.user.models import User

from django import forms
from django.utils.translation import gettext_lazy as _


class CustomUserLoginForm(forms.Form):
    email = forms.EmailField(label=_("Email"), widget=forms.EmailInput)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')
