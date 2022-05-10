from service_objects.services import Service, forms

from models_module.models import Photo


class GetPhotoDetailsService(Service):
    photo_id = forms.IntegerField(required=True, min_value=1)

    def process(self):
        self.result = self._get_photo_by_id()

        return self

    def _get_photo_by_id(self):
        photo = Photo.objects.get(id=self.cleaned_data.get('photo_id'))

        return photo