from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from web_site.views.user import registration, email_login, logout, change, change_key, personal_profile
from web_site.views.main_pages import main_page, personal_cabinet
from web_site.views.photo import upload

app_name = 'web_site'

urlpatterns = [
    path('', main_page.HomeView.as_view(), name='home'),
    path('api-token/', change_key.GenerateNewTokenView.as_view(), name='api_token'),
    path('register/', registration.UserRegistrationView.as_view(), name='register'),
    path('login/', email_login.UserLoginView.as_view(), name='login'),
    path('logout/', logout.UserLogoutView.as_view(), name='logout'),
    path('profile/', personal_profile.UserPersonalProfileView.as_view(), name='profile'),
    path('cabinet/', personal_cabinet.CabinetView.as_view(), name='cabinet'),
    path('change/', change.UserChangeView.as_view(), name='change'),
    path('upload/', upload.PhotoUploadView.as_view(), name='photo_upload')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
