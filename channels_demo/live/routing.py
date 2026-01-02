from django.urls import re_path
from .consumers import CounterConsumer

websocket_urlpatterns = [
    re_path(r"ws/counter/", CounterConsumer.as_asgi()),
]
