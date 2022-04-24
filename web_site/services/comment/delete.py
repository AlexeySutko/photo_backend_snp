import pdb

from django.core.exceptions import ValidationError
from django.db.models import F
from service_objects.services import Service, forms

from models_module.models import Photo
from models_module.models.comment.models import Comment


class Delete(Service):
    user_id = forms.IntegerField(min_value=1)
    comment_id = forms.IntegerField(min_value=1)

    def process(self):
        self.result = self._delete()
        return self

    def _delete(self):
        if self._is_comment_present() and self._is_user_owner() and not self._is_thread_present():
            comment = Comment.collection.get(pk=self.cleaned_data.get('comment_id'))
            self._update_photo_comment_count()
            comment.delete()
            return True
        return False

    def _is_comment_present(self):
        if Comment.collection.filter(pk=self.cleaned_data.get('comment_id')).exists():
            return True
        else:
            self.add_error(
                'comment_id',
                ValidationError(f"Comment with id = {self.cleaned_data['comment_id']} does not exists!")
            )
            return False

    def _is_user_owner(self):
        if Comment.collection.get(
                pk=self.cleaned_data.get('comment_id')).user.pk == self.cleaned_data.get('user_id'):
            return True
        self.add_error(
            'user_id',
            ValidationError(f"User with id = {self.cleaned_data.get('user_id')} don't have permission for this action")
        )
        return False

    def _is_thread_present(self):
        if Comment.collection.get(id=self.cleaned_data.get('comment_id')).comments.all():
            self.add_error(
                'comment_id',
                ValidationError(
                    f"Cant delete a comment id = {self.cleaned_data['comment_id']}  because it has a thread")
            )
            return True
        return False

    def _update_photo_comment_count(self):
        comment = Comment.collection.get(id=self.cleaned_data.get('comment_id'))
        if comment.owner.__class__.__name__ == 'Comment':
            photo = Photo.objects.get(id=comment.owner.owner.id)
        elif comment.owner.__class__.__name__ == 'Photo':
            photo = Photo.objects.get(id=comment.owner.id)
        else:
            return self

        photo.comment_count = F('comment_count') - 1
        photo.save(update_fields=["comment_count"])
