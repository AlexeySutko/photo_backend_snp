from models_module.models.user.models import User

from django import forms
from django.utils.translation import gettext_lazy as _


class CustomUserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Repeat password"), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError(_('Passwords don\'t match.'))
        return cd['password2']
