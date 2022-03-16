from django.core.exceptions import ValidationError
from service_objects.services import Service, forms
from service_objects.fields import ModelField

from models_module.models.user.models import User
from models_module.models.like.models import Like
from models_module.models.photo.models import Photo

from django.shortcuts import get_object_or_404


class IsLiked(Service):
    photo_id = forms.IntegerField(min_value=1)
    current_user = ModelField(User)

    def process(self):
        return Like.objects.filter(photo_id=outcome.result.object_list[0].id, user_id=request.user.pk).exists()