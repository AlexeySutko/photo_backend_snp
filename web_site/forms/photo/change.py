from models_module.models.photo.models import Photo

from django.utils.translation import gettext_lazy as _
from django import forms


class PhotoChangeForm(forms.ModelForm):
    future_name = forms.CharField(label=_('Name'), required=False)
    future_image = forms.ImageField(label=_('Image'), required=False)
    future_description = forms.CharField(required=False, widget=forms.Textarea,
                                         label=_('Description'),)

    class Meta:
        model = Photo
        fields = ('future_name', 'future_image', 'future_description',)
