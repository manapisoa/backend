from django.urls import re_path
from .consumers import NotifConsumers
websocket_urlpatterns = [re_path(r'ws/notifs/$',NotifConsumers.as_asgi())]