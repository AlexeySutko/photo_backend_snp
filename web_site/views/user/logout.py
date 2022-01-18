from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import View


class UserLogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(redirect_to='/home')
