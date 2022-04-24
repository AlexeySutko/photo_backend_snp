from django.contrib.contenttypes.models import ContentType
from service_objects.services import Service, forms

from models_module.models.comment.models import Comment


class GetCollection(Service):
    parent = forms.CharField()
    parent_id = forms.IntegerField(min_value=1)

    def process(self):
        if self.cleaned_data.get('parent') == 'photo':
            self.result = self._comments()
        else:
            self.result = self._answers()
            return self

    def _comments(self):
        comments = Comment.collection.filter(object_id=self.cleaned_data.get('parent_id'),
                                             content_type=ContentType.objects.get(model=self.cleaned_data.get('parent')))
        return comments

    def _answers(self):
        answers = Comment.collection.filter(object_id=self.cleaned_data.get('parent_id'),
                                            content_type=ContentType.objects.get(model=self.cleaned_data.get('parent')))
        return answers
