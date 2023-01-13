from django.urls import path
from . import users

websocket_urlpatterns=[
    path('ws/<str:room_name>/',users.ChatConsumer.as_asgi()),
]