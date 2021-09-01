from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/connect', consumers.NotificationsConsumer.as_asgi()),
]
