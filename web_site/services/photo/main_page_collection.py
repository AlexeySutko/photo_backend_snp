from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from service_objects.services import Service, forms

from models_module.models.user.models import User
from models_module.models.like.models import Like
from models_module.models.photo.models import Photo


class MainPageCollection(Service):
    user_id = forms.IntegerField(required=False)
    search_string = forms.CharField(required=False)
    sorted_by = forms.CharField(required=False)
    page = forms.IntegerField(min_value=1, required=False)

    def process(self):
        self.result = self._collection
        return self

    @property
    def _collection(self):
        page = Paginator(self._photos, 6).page(self.cleaned_data.get('page') or 1)
        for photo in page.object_list:
            setattr(photo, "is_liked",
                    photo.likes.filter(user_id=self.cleaned_data.get("user_id")).exists())
        return page

    @property
    def _photos(self):
        photos = Photo.objects.filter(state='Approved')
        if self.cleaned_data.get('search_string'):
            photos = photos.filter(name__icontains=self.cleaned_data.get('search_string'), state='Approved')
        if self.cleaned_data.get('sorted_by'):
            photos = photos.order_by(self.cleaned_data.get('sorted_by'))
        import pdb
        # pdb.set_trace()
        return photos.prefetch_related('likes')

    def _is_photos_present(self):
        if not self._photos and self.cleaned_data.get('search_string'):
            self.add_error(
                'search_string',
                ValidationError(f"No photos were found with {self.cleaned_data.get('search_string')}")
            )
            return False
        elif not self._photos:
            self.add_error(
                error=ValidationError("Site has no photos for now")
            )
            return False
        return True

    # def _get_item_collection(self):
    #     # cd_offset = self.cleaned_data['offset']
    #     self.query = Photo.objects.filter(state='Approved') #  [cd_offset:self.COUNT]
    #
    #     return self.query
    #
    # def _get_item_collection_with_search(self):
    #     cd_search_string = self.cleaned_data['search_string']
    #     # cd_search_flag = self.cleaned_data['search_flag']
    #     self.query = Photo.objects.none()
    #     self.query = Photo.objects.filter(state='Approved', name__contains=cd_search_string)
    #     self.query |= Photo.objects.filter(state='Approved', description__contains=cd_search_string)
    #     self.query |= Photo.objects.filter(state='Approved', owner__contains=cd_search_string)
    #     return self.query.distinct()
    #
    # def _sort_item_collection(self):
    #     cd_sort_flag = self.cleaned_data['sort_flag']
    #     self.query = self.query.order_by(cd_sort_flag)
    #
    #     return self.query
