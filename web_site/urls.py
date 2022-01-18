from django.urls import path

from web_site.views.user import registration, login, logout
from web_site.views.main_pages import main_page

app_name = 'web_site'

urlpatterns = [
    path('home/', main_page.MainView.as_view(), name='index'),
    path('register/', registration.UserRegistrationView.as_view(), name='register'),
    path('login/', login.UserLoginView.as_view(), name='login'),
    path('logout/', logout.UserLogoutView.as_view(), name='logout'),
]
