from service_objects.services import Service, forms

from models_module.models.photo.models import Photo

"""
Service layer for logic related to creating photos
"""


class CreatePhoto(Service):
    image = forms.ImageField()
    name = forms.CharField()
    description = forms.CharField()

    def process(self):
        owner = self.initial['user']
        image = self.cleaned_data['image']
        name = self.cleaned_data['name']
        description = self.cleaned_data['description']

        self.photo = Photo.objects.create(owner=owner, image=image,
                                          name=name, description=description)
        return self.photo.save()
