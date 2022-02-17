from models_module.models.photo.models import Photo

from django.shortcuts import render
from django.views.generic.detail import DetailView


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photo_details.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


