import json
import pdb

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import HttpResponse, render
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

        if outcome.is_valid():
            return JsonResponse("Comment deleted", status=200, safe=False)
        else:
            return JsonResponse(outcome.errors, status=400, safe=False)

    def put(self, request, *args, **kwargs):
        outcome = Change.execute({
            'user_id': request.user.pk,
            'comment_id': kwargs.get('comment_id'),
            'comment_text': json.loads(request.body)['comment_text']
        })
        return render(request, template_name="_comment.html", context={"comment": outcome.result})
