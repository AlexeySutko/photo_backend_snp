from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from fsm_admin2.admin import FSMTransitionMixin

from models_module.models.comment.models import Comment

from imagekit.admin import AdminThumbnail


class CommentAdmin(FSMTransitionMixin, admin.ModelAdmin):
    model = Comment

    list_display = ('owner', 'object_id', 'user', 'text')
    list_display_links = ('user', 'object_id')

    readonly_fields = ('object_id', 'content_type', 'owner',)

    fields = ['user', 'text']
