from django.forms import ModelForm
from models_module.models.photo.models import Photo


class PhotoModerationForm(ModelForm):

    class Meta:
        model = Photo
        fields = ('future_name', 'future_image', 'future_description')