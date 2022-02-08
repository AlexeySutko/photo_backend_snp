from models_module.models.user.models import User
from web_site.forms.user.login import CustomUserLoginForm
from django.utils.translation import gettext_lazy as _
from django.views.generic.base import View
from django.contrib.auth import login, authenticate
from django.shortcuts import render, HttpResponse, HttpResponseRedirect

"""
    View used to login user with email and password
"""


class UserLoginView(View):
    template_name = 'modal_login.html'
    form_class = CustomUserLoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'login_form': form})

    def post(self, request):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            try:
                user = authenticate(request,
                                    email=form.cleaned_data['email'],
                                    password=form.cleaned_data['password'])
            except Exception:
                form.add_error(None, "Something went wrong")

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')

            else:
                form.add_error(None, "Something went wrong")

        return HttpResponseRedirect('/')
