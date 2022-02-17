from models_module.models.user.models import User
from django import forms
from imagekit.forms.fields import ImageField as ImageKitField
from django.utils.translation import gettext_lazy as _


class CustomUserChangeForm(forms.ModelForm):
    avatar = ImageKitField(label=_('Avatar'))
    first_name = forms.CharField(label=_('First name'))
    last_name = forms.CharField(label=_('Last name'))
    bio = forms.CharField(widget=forms.Textarea, label=_('Bio'))
    birth_date = forms.DateField(label=_('date of birth'),
                                 widget=forms.SelectDateWidget(years=[x for x in range(1940, 2011)]))

    class Meta:
        model = User
        fields = ['avatar', 'first_name', 'last_name', 'bio', 'birth_date']
