from web_site.forms.user.registration import CustomUserRegistrationForm
from web_site.services.user.create import CreateUser

from django.contrib.auth import login, authenticate
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import CreateView

"""
    View used to register new users 
"""


class UserRegistrationView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserRegistrationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'registration_form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            try:
                CreateUser.execute(self.request.POST)
                user = authenticate(request,
                                    email=form.cleaned_data['email'],
                                    password=form.cleaned_data['password'])
                login(self.request, user)
                return HttpResponseRedirect('/home/')
            except Exception:
                form.add_error(None, "Something went wrong")

        return render(request, self.template_name, {'registration_form': form})
