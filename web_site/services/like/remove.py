from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from service_objects.services import Service, forms
from service_objects.fields import ModelField

from models_module.models import Photo
from models_module.models.user.models import User
from models_module.models.like.models import Like


class Remove(Service):
    photo_id = forms.IntegerField(min_value=1)
    current_user = ModelField(User)

    def process(self):
        if self._is_like_present():
            Like.objects.filter(user=self.cleaned_data['current_user'],
                                photo_id=self.cleaned_data['photo_id']).delete()
            self._get_like_counter()
        return self

    def _is_like_present(self):
        if Like.objects.filter(user=self.cleaned_data['current_user'],
                               photo_id=self.cleaned_data['photo_id']).exists():

            return True
        else:
            self.add_error(
                'photo_id',
                ValidationError(f"Photo with id = {self.cleaned_data['photo_id']} has not been liked")
            )
            return False

    def _get_like_counter(self):
        photo = get_object_or_404(Photo, pk=self.cleaned_data['photo_id'])
        self.number_of_likes = photo.likes.count()
        return self.number_of_likes
