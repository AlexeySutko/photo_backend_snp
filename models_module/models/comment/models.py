from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

from models_module.managers.comment.manager import CommentManager
from models_module.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='comments', related_query_name='comments')
    text = models.CharField(max_length=500, verbose_name="Comment text")

    # Recreate error with "wrong" names
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name="content_type_comments")
    object_id = models.PositiveIntegerField()
    owner = GenericForeignKey('content_type', 'object_id')

    comment_count = models.IntegerField(default=0, null=True)

    comments = GenericRelation('Comment')

    collection = CommentManager()

    class Meta:
        db_table = 'comments'
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
