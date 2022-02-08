from models_module.models.user.models import User

from web_site.services.user.generate_new_token import generate_new_token

from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

"""
    View used to revoke previous and generate new token for the user
"""


class GenerateNewTokenView(LoginRequiredMixin, UpdateView):
    model = User
    success_url = "/cabinet/"

    def get(self, request, *args, **kwargs):
        generate_new_token(request)
        return HttpResponseRedirect(redirect_to='/cabinet/')
