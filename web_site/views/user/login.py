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
            user = authenticate(request,
                                email=form.cleaned_data['email'],
                                password=form.cleaned_data['password'])

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home/')

        return HttpResponseRedirect('/home/')

