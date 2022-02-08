from django.forms import ModelForm
from models_module.models.photo.models import Photo


class PhotoChangeForm(ModelForm):

    class Meta:
        model = Photo
        fields = ('name', 'image', 'description', 'publish_date', 'owner')