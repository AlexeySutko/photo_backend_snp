from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required


class UserLogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(redirect_to='/')
