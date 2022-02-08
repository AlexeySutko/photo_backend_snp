from django.forms import ModelForm
from models_module.models.photo.models import Photo


class PhotoCreationForm(ModelForm):

    class Meta:
        model = Photo
        fields = ('name', 'image', 'description', 'publish_date', 'state', 'owner')
