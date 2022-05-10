from django.core.paginator import Paginator
from service_objects.services import Service, forms

from models_module.models import Photo
from photo_backend_snp import settings


class GetPhotoCollectionService(Service):
    search_string = forms.CharField(required=False)
    sorted_by = forms.CharField(required=False)
    page = forms.IntegerField(min_value=1, required=False)

    def process(self):
        self.result = self._collection()
        return self

    def _collection(self):
        page = Paginator(self._photos(), per_page=settings.MAIN_PAGE_COLLECTION_OBJECT_COUNT)\
            .page(self.cleaned_data.get('page') or 1)
        return page

        # return self._photos()

    def _photos(self):
        photos = Photo.objects.filter(state='Approved').order_by('publish_date')
        if self.cleaned_data.get('search_string'):
            photos = photos.filter(name__icontains=self.cleaned_data.get('search_string'))
            photos = photos.filter(description__icontains=self.cleaned_data.get('search_string'))
        if self.cleaned_data.get('sorted_by'):
            photos = photos.order_by(self.cleaned_data.get('sorted_by'))
        return photos.select_related('owner')
