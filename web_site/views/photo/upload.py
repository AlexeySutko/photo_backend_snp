from web_site.forms.photo.upload import PhotoUploadForm
from web_site.services.photo.upload import CreatePhoto

from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

"""
    View used to upload photo
"""


class PhotoUploadView(LoginRequiredMixin, CreateView):
    template_name = 'photo_upload.html'
    form_class = PhotoUploadForm
    success_url = "/cabinet/"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'upload_form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST, self.request.FILES)
        if form.is_valid():
            try:
                CreatePhoto.execute(self.request.POST, files=self.request.FILES,
                                    initial={'user': self.request.user})
                return HttpResponseRedirect('/cabinet/')
            except Exception:
                form.add_error(None, "Something went wrong")

        return render(request, self.template_name, {'upload_form': form})
