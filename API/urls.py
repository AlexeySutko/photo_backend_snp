from django.urls import path
from django.conf import settings

from API.views.photo.collection import PhotoCollectionView
from API.views.user.details import UserDetailsView
app_name = 'API'

urlpatterns = [
    path('v1/photo_collection/', PhotoCollectionView.as_view()),
    path('v1/user_details/', UserDetailsView.as_view()),
]