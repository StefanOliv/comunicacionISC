from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/<str:canal_name>/', consumers.ChatConsumer.as_asgi()),
    path('msg/<int:id>/', consumers.PersonalConsumer.as_asgi()),
]