import json
import pdb

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db.models import F
from service_objects.services import Service, forms

from models_module.models import Photo, User
from models_module.models.comment.models import Comment
from photo_backend_snp.settings import REDIS_INSTANCE


class Create(Service):
    user_id = forms.IntegerField(min_value=1)
    parent = forms.CharField()
    parent_id = forms.IntegerField(min_value=1)
    photo_id = forms.IntegerField(min_value=1)
    comment_text = forms.CharField()

    def process(self):
        self.result = self._create()
        self._update_comment_count_with_recursion()
        return self

    def _create(self):
        comment = Comment(content_type=ContentType.objects.get(model=self.cleaned_data.get('parent')),
                          object_id=self.cleaned_data.get('parent_id'),
                          user_id=self.cleaned_data.get('user_id'),
                          text=self.cleaned_data.get('comment_text'))
        comment.save()
        return comment

    def _is_comment_present(self):
        if self.cleaned_data['parent'] == 'comment' and Comment.collection.filter(
                id=self.cleaned_data['parent_id']).exists():
            return True
        self.add_error(
            'parent_id',
            ValidationError(f"Comment with id = {self.cleaned_data['parent_id']} does not exists!")
        )
        return False

    def _is_photo_present(self):
        if self.cleaned_data['parent'] == 'photo' and Photo.objects.filter(
                id=self.cleaned_data.get('parent_id')).exists():
            return True
        self.add_error(
            'photo_id',
            ValidationError(f"Photo with id = {self.cleaned_data.get('photo_id')} does not exists!")
        )
        return False

    def _update_comment_count_with_recursion(self):
        photo = Photo.objects.get(id=self.cleaned_data['photo_id'])
        counter = photo.comments.count()

        def func(comment, counter):
            if comment.comments.all():
                counter += comment.comments.count()
                comment.comment_count = comment.comments.count()
                comment.save(update_fields=["comment_count"])
                for answer in comment.comments.all():
                    counter = func(answer, counter)
                    return counter
            else:
                return counter

        for comment in photo.comments.all():
            counter = func(comment, counter)

        photo.comment_count = counter
        photo.save(update_fields=["comment_count"])

    def _update_comment_count_with_number(self):
        photo = Photo.objects.get(id=self.cleaned_data['photo_id'])
        photo.comment_count = F('comment_count') + 1
        photo.save(update_fields=["comment_count"])

    def _send_notification(self, photo):
        channel_layer = get_channel_layer()
        user = User.objects.get(id=self.cleaned_data.get('user_id'))
        async_to_sync(channel_layer.send)(REDIS_INSTANCE.get(f"private_for_{photo.owner_id}").decode("utf-8"), {
            "type": "photo_approval_notification",
            "payload": json.dumps({
                'type': "comment",
                'photo_name': photo.name,
                'comment_owner': user.get_full_name(),
            }),
        })
