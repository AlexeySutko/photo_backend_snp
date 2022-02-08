from models_module.models.user.models import User
from django.shortcuts import get_object_or_404, render
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.authtoken.models import Token


class UserPersonalProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user_details.html'
    context_object_name = 'user'
    extra_context = 'token'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['user'] = self.request.session.get('user')
        context['token'] = Token.objects.get(user=self.request.session.get('user'))

        return render(request, template_name=self.template_name, context=context)
