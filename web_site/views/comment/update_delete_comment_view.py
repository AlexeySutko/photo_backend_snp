import json
import pdb

from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt


from web_site.services.comment.delete import Delete
from web_site.services.comment.change import Change


@method_decorator(csrf_exempt, name='dispatch')
class UpdateDeleteCommentView(View):
    def delete(self, request, *args, **kwargs):
        # Comment is up for deletion until
        # it has an answers
        outcome = Delete.execute({
            'user_id': request.user.pk,
            'comment_id': kwargs.get('comment_id')
        })
        return HttpResponse(outcome.result)

    def put(self, request, *args, **kwargs):
        outcome = Change.execute({
            'user_id': request.user.pk,
            'comment_id': kwargs.get('comment_id'),
            'comment_text': json.loads(request.body)['comment_text']
        })
        return HttpResponse(outcome.result)
