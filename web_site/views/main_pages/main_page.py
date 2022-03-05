from models_module.models.photo.models import Photo
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

"""
    Placeholder for a main page showing photos
"""


class HomeView(ListView):
    model = Photo
    template_name = 'main_page.html'
    context_object_name = 'photo_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['photo_list'] = Photo.objects.filter(state='Approved')
        paginator = Paginator(context['photo_list'], 6)
        page = self.request.GET.get('page')
        try:
            context['photo_list'] = paginator.page(page)
        except PageNotAnInteger:
            context['photo_list'] = paginator.page(1)
        except EmptyPage:
            context['photo_list'] = paginator.page(paginator.num_pages)

        return context

    def post(self, request, *args, **kwargs):
        
