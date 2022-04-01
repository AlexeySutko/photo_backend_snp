from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from models_module.models import Photo
from web_site.services.photo.personal_cabinet_collection import PersonalCabinetCollection


@method_decorator(csrf_exempt, name='dispatch')
class CabinetView(LoginRequiredMixin, View):
    model = Photo
    template_name = 'personal_cabinet.html'
    context_object_name = 'object_list'

    def get(self, request, *args, **kwargs):
        outcome = PersonalCabinetCollection.execute(dict(request.GET.items()) | {"user_id": request.user.pk})
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return render(request, template_name='object_collection.html', context={'object_list': outcome.result})
        else:
            return render(request, template_name=self.template_name, context={'object_list': outcome.result})
