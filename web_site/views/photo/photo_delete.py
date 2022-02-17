from models_module.models.photo.models import Photo

from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponseRedirect, redirect, get_object_or_404


class PhotoChangeView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = "/cabinet/"

    def get(self, request, *args, **kwargs):
        instance = get_object_or_404(Photo, pk=kwargs['pk'])

        return redirect("/cabinet/")
