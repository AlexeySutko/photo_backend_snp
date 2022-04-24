import pdb

from django.core.exceptions import ValidationError
from service_objects.services import Service, forms

from models_module.models.comment.models import Comment


class Change(Service):
    user_id = forms.IntegerField(min_value=1)
    comment_id = forms.IntegerField(min_value=1)
    comment_text = forms.CharField(max_length=500)

    def process(self):
        self.result = self._change()
        pdb.set_trace()
        return self

    def _change(self):
        comment = Comment.collection.get(pk=self.cleaned_data.get('comment_id'))
        if self.cleaned_data.get('comment_text'):
            pdb.set_trace()
            comment.text = self.cleaned_data.get('comment_text')
        comment.save()
        return comment

    def _is_comment_present(self):
        if Comment.collection.filter(object_id=self.cleaned_data.get('comment_id')).exists():
            return True
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
