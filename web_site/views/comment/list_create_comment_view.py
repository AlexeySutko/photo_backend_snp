import json
import pdb

from django.contrib.contenttypes.models import ContentType
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from models_module.models.comment.models import Comment
from web_site.services.comment.create import Create
from web_site.services.comment.delete import Delete
from web_site.services.comment.change import Change
from web_site.services.comment.get_collection import GetCollection


@method_decorator(csrf_exempt, name='dispatch')
class ListCreateCommentView(View):
    model = Comment

    def get(self, request, *args, **kwargs):
        outcome = GetCollection.execute({"parent_id": kwargs.get("parent_id"),
                                         "parent": kwargs.get("parent"),
                                         "page": request.GET.get('page')})

        return render(request, template_name='comments.html', context={'comment_list': outcome.result})

    def post(self, request, *args, **kwargs):
        outcome = Create.execute({"user_id": request.user.pk,
                                  "parent_id": request.POST.get('parent_id'),
                                  "parent": request.POST.get('parent'),
                                  "comment_text": request.POST.get("comment_text"),
                                  "photo_id": kwargs.get('parent_id')})

        return render(request, template_name="_comment.html", context={"comment": outcome.result})
