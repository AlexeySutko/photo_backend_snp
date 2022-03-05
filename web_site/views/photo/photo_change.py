from models_module.models.photo.models import Photo
from web_site.forms.photo.change import PhotoChangeForm

from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponseRedirect, render, get_object_or_404


class PhotoChangeView(LoginRequiredMixin, UpdateView):
    model = Photo
    template_name = 'change_photo.html'
    form_class = PhotoChangeForm
    success_url = "/cabinet/"

    def get(self, request, *args, **kwargs):
        instance = get_object_or_404(Photo, pk=self.kwargs['pk'])
        form = self.form_class(instance=instance)
        return render(request, self.template_name, {'change_form': form})

    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(Photo, pk=self.kwargs['pk'])
        form = self.form_class(self.request.POST, self.request.FILES, instance=instance)
        if form.is_valid():
            instance.photo_on_moderation()
            form.save()
            instance.save()
            return HttpResponseRedirect('/cabinet/')

        return render(request, self.template_name, {'change_form': form})
