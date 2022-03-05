from models_module.models.photo.models import Photo
from models_module.models.user.models import User
from models_module.models.like.models import Like

from django.shortcuts import get_object_or_404

class IsLiked:

    @staticmethod
    def is_liked(user, photo):
        photo = get_object_or_404(Photo, pk=photo.id)
        user = get_object_or_404(User, pk=user.id)

        for like in photo.likes.all():
            like.user.id
        for like in user.likes.all():
            like.photo_id

        if Like.objects.filter(user=user, photo=photo):
            return True
        else:
            return False
