from photo_backend_snp import settings
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from service_objects.services import Service, forms

from models_module.models.user.models import User
from models_module.models.like.models import Like
from models_module.models.photo.models import Photo


class PersonalCabinetCollection(Service):
    user_id = forms.IntegerField(required=False)
    search_string = forms.CharField(required=False)
    sorted_by = forms.CharField(required=False)
    page = forms.IntegerField(min_value=1, required=False)

    def process(self):
        self.result = self._collection
        return self

    @property
    def _collection(self):
        page = Paginator(self._photos, settings.PERSONAL_CABINET_COLLECTION_OBJECT_COUNT)\
            .page(self.cleaned_data.get('page') or 1)
        for photo in page.object_list:
            setattr(photo, "is_liked",
                    bool(list(filter(lambda x: x.user_id == self.cleaned_data.get("user_id"), photo.likes.all()))))
        return page

    @property
    def _photos(self):
        photos = Photo.objects.filter(owner_id=self.cleaned_data.get("user_id"))
        if self.cleaned_data.get('search_string'):
            photos = photos.filter(name__icontains=self.cleaned_data.get('search_string'))
            photos = photos.filter(description__icontains=self.cleaned_data.get('search_string'))
        if self.cleaned_data.get('sorted_by'):
            photos = photos.order_by(self.cleaned_data.get('sorted_by'))
        return photos.prefetch_related('likes').select_related('owner')
