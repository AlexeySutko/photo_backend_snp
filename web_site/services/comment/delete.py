import pdb

from django.core.exceptions import ValidationError
from service_objects.services import Service, forms

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
            self.comment_parent = comment.owner
            self._update_comment_count_with_recursion()
            return True
        return False

    def _is_comment_present(self):
        if Comment.collection.filter(pk=self.cleaned_data.get('comment_id')).exists():
            return True
        else:
            self.add_error(
                'error',
                ValidationError(f"Comment with id = {self.cleaned_data['comment_id']} does not exists!")
            )
            return False

    def _is_user_owner(self):
        if Comment.collection.get(
                pk=self.cleaned_data.get('comment_id')).user.pk == self.cleaned_data.get('user_id'):
            return True
        self.add_error(
            'error',
            ValidationError(f"User with id = {self.cleaned_data.get('user_id')} don't have permission for this action")
        )
        return False

    def _is_thread_present(self):
        if Comment.collection.get(pk=self.cleaned_data.get('comment_id')).comments.all():
            self.add_error(
                'error',
                ValidationError(
                    f"Cant delete a comment id = {self.cleaned_data['comment_id']}  because it has a thread")
            )
            return True
        return False

    def _update_comment_count_with_recursion(self):
        comment = self.comment_parent
        counter = comment.comments.count()

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

        for answer in comment.comments.all():
            counter = func(answer, counter)

        comment.comment_count = counter
        comment.save(update_fields=["comment_count"])
