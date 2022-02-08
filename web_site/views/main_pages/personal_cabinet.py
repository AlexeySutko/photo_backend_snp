from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class CabinetView(LoginRequiredMixin, ListView):
    template_name = 'personal_cabinet.html'
    context_object_name = 'photo_list'
    paginate_by = 3

    def get_queryset(self):
        return self.request.user.photos.all()
