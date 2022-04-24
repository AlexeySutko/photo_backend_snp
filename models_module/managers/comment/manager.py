from django.db import models


class CommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().prefetch_related('comments').select_related('user')
