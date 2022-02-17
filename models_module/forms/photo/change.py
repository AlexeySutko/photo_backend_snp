from django.forms import ModelForm
from models_module.models.photo.models import Photo


class PhotoChangeForm(ModelForm):

    def image_tag(self):
        from django.utils.html import escape
        return u'<img src="%s" />' % escape(self.image.url)
    image_tag.short_description = 'Image preview'
    image_tag.allow_tags = True

    class Meta:
        model = Photo
        fields = ('name', 'image', 'description', 'publish_date', 'owner', 'mark_as_deleted_at')
        readonly_fields = ('image_tag',)
