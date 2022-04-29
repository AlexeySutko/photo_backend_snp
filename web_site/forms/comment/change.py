from models_module.models.comment.models import Comment

from django.utils.translation import gettext_lazy as _
from django import forms


class CommentChangeForm(forms.ModelForm):
    comment_text = forms.CharField(widget=forms.Textarea,
                                   label=_('New comment'), )

    class Meta:
        model = Comment
        fields = ('comment_text')
