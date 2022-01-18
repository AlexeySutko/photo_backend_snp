from models_module.models.user.models import User
from web_site.forms.user.login import CustomUserLoginForm
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic.list import ListView

"""
    Placeholder for a main page showing photos
"""

class MainView(ListView):
    template_name = 'main_page.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        return User.objects.order_by('-is_superuser')