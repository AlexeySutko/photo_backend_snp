from web_site.forms.user.change import CustomUserChangeForm

from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

"""
    View used to change user profile 
"""


class UserChangeView(LoginRequiredMixin, UpdateView):
    template_name = 'change_user.html'
    form_class = CustomUserChangeForm
    success_url = "/cabinet/"

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=request.user)
        avatar = request.FILES.get('avatar')
        return render(request, self.template_name, {'change_form': form, 'avatar': avatar})

    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST, self.request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/cabinet/')

        return render(request, self.template_name, {'change_form': form})
