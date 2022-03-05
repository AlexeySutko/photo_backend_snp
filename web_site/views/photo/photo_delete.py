from models_module.models.photo.models import Photo

from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = "/cabinet/"

    def get(self, request, *args, **kwargs):
        instance = get_object_or_404(Photo, pk=kwargs['pk'])
        instance.photo_on_deletion()
        instance.save()
        return redirect("/cabinet/")
