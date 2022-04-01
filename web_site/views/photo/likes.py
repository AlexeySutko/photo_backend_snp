import json

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from web_site.services.like.create import Create
from web_site.services.like.remove import Remove
from web_site.services.like.is_liked import IsLiked

# from models_module.models.user.models import User
# from models_module.models.photo.models import Photo


from django.views import View
from django.http import JsonResponse
from django.shortcuts import render


@method_decorator(csrf_exempt, name='dispatch')
class LikeView(View):

    def post(self, request, *args, **kwargs):
        outcome = Create.execute({
            'current_user': request.user,
            'photo_id': json.loads(request.body)['photo_id']
        })
        if outcome.is_valid():
            return JsonResponse(outcome.number_of_likes, status=200, safe=False)
        else:
            return JsonResponse(outcome.errors, status=400, safe=False)

    def delete(self, request, *args, **kwargs):
        outcome = Remove.execute({
            'current_user': request.user,
            'photo_id': json.loads(request.body)['photo_id']
        })
        if outcome.is_valid():
            return JsonResponse(outcome.number_of_likes, status=200, safe=False)
        else:
            return JsonResponse(outcome.errors, status=400, safe=False)
