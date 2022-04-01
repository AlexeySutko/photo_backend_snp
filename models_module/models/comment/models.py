from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from models_module.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='comments', related_query_name='comments')
    text = models.TextField(verbose_name="Comment text")

    owner_id = models.PositiveIntegerField()
    owner_type = models.ForeignKey(ContentType, on_delete=models.PROTECT, related_name="owner_type_comments")
    owner = GenericForeignKey('owner_type', 'owner_id')

    class Meta:
        db_table = 'comments'
        verbose_name = "comment"
        verbose_name_plural = "comments"
