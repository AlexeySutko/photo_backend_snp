from models_module.models.photo.models import Photo
from django.views.generic.list import ListView

"""
    Placeholder for a main page showing photos
"""


class HomeView(ListView):
    template_name = 'main_page.html'
    context_object_name = 'photo_list'
    paginate_by = 6

    def get_queryset(self):
        return Photo.objects.order_by('-publish_date')
