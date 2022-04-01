import json

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from models_module.models import Photo
from web_site.services.photo.main_page_collection import MainPageCollection

from django.views.generic.list import View
from django.shortcuts import render

"""
    Placeholder for a main page showing photos
"""


@method_decorator(csrf_exempt, name='dispatch')
class HomeView(View):
    model = Photo
    template_name = 'main_page.html'
    context_object_name = 'object_list'

    def get(self, request, *args, **kwargs):
        outcome = MainPageCollection.execute(dict(request.GET.items()) | {"user_id": request.user.pk})
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return render(request, template_name='object_collection.html', context={'object_list': outcome.result})
        else:
            return render(request, template_name=self.template_name, context={'object_list': outcome.result})
