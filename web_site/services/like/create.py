import asyncio
import json
import pdb

from asgiref.sync import async_to_sync, sync_to_async
from channels.layers import get_channel_layer
from django.core.exceptions import ValidationError
from service_objects.services import Service, forms
from service_objects.fields import ModelField
from django.db.models import F

from models_module.models.user.models import User
from models_module.models.like.models import Like
from models_module.models.photo.models import Photo
from photo_backend_snp.settings import REDIS_INSTANCE


class Create(Service):
    photo_id = forms.IntegerField(min_value=1)
    current_user = ModelField(User)

    def process(self):
        if not self._is_like_present():
            self.like = Like.objects.create(user=self.cleaned_data['current_user'],
                                            photo_id=self.cleaned_data['photo_id'])
            self._increment_like_count()
            self._get_likes_count()
            self._send_notification()
        return self

    def _is_like_present(self):
        if Like.objects.filter(user=self.cleaned_data['current_user'],
                               photo_id=self.cleaned_data['photo_id']).exists():
            self.add_error(
                'photo_id',
                ValidationError(f"Photo with id = {self.cleaned_data['photo_id']} is already liked")
            )
            return True

        return False

    def _increment_like_count(self):
        photo = Photo.objects.get(id=self.cleaned_data['photo_id'])
        photo.likes_count = F("likes_count") + 1
        photo.save(update_fields=["likes_count"])

    def _get_likes_count(self):
        photo = Photo.objects.get(id=self.cleaned_data['photo_id'])
        self.number_of_likes = photo.likes_count
        return self.number_of_likes

    def _send_notification(self):
        photo = Photo.objects.get(id=self.cleaned_data['photo_id'])
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.send)(REDIS_INSTANCE.get(f"private_for_{photo.owner_id}").decode("utf-8"), {
            "type": "liked_notification",
            "payload": json.dumps({
                'type': "photo_liked",
                'photo_name': photo.name,
                'user': self.cleaned_data['current_user'].get_full_name(),
            }),
        })
