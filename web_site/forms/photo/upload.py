from django.forms import ModelForm
from django import forms
from models_module.models.photo.models import Photo


class PhotoUploadForm(ModelForm):
    name = forms.CharField()
    image = forms.ImageField()
    description = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = Photo
        fields = ('name', 'image', 'description')
