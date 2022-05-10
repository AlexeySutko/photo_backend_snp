from django.urls import path

from .consumers import WSConsumer

app_name = 'notifications'

ws_urlpatterns = [
    path('/notifications/', WSConsumer.as_asgi())
]
