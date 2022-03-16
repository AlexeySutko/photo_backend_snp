import json

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from models_module.models import Photo
from web_site.services.photo.main_page_collection import MainPageCollection

from django.views.generic.list import View
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

"""
    Placeholder for a main page showing photos
"""


@method_decorator(csrf_exempt, name='dispatch')
class HomeView(View):
    model = Photo
    template_name = 'main_page.html'
    context_object_name = 'photo_list'

    def get(self, request, *args, **kwargs):
        outcome = MainPageCollection.execute(dict(request.GET.items()) | {"user_id": request.user.pk})
        if outcome.is_valid():
            return render(request, template_name=self.template_name, context={'photo_list': outcome.result})
        else:
            return render(request, template_name=self.template_name, context={'photo_list': outcome.errors})