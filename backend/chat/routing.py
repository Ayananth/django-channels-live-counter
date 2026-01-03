from django.urls import re_path
from .consumers import GroupTestConsumer

websocket_urlpatterns = [
    re_path(r"ws/group-test/$", GroupTestConsumer.as_asgi()),
]
