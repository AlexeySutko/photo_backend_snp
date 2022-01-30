from django.urls import path

from web_site.views.user import registration, email_login, logout
from web_site.views.main_pages import main_page

app_name = 'web_site'

urlpatterns = [
    path('', main_page.HomeView.as_view(), name='home'),
    path('register/', registration.UserRegistrationView.as_view(), name='register'),
    path('login/', email_login.UserLoginView.as_view(), name='login'),
    path('logout/', logout.UserLogoutView.as_view(), name='logout'),
]
