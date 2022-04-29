import pdb

from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator
from service_objects.services import Service, forms

from models_module.models.comment.models import Comment
from photo_backend_snp import settings


class GetCollection(Service):
    parent = forms.CharField()
    parent_id = forms.IntegerField(min_value=1)
    page = forms.IntegerField(min_value=1, required=False)

    def process(self):
        if self.cleaned_data.get('parent') == 'photo':
            self.result = self._collection()
        else:
            self.result = self._comments()
        return self

    def _collection(self):
        page = Paginator(self._comments(), settings.COMMENT_COLLECTION_OBJECT_COUNT) \
            .page(self.cleaned_data.get('page') or 1)

        return page

    def _comments(self):
        comments = Comment.collection.filter(object_id=self.cleaned_data.get('parent_id'),
                                             content_type=ContentType.objects.get(
                                                 model=self.cleaned_data.get('parent')))
        return comments
