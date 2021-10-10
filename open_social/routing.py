from django.urls import re_path

from app_messages.consumers import MsgConsumer

websocket_urlpatterns = [
    re_path(r'^ws/messages/(?P<id>[a-zA-Z0-9_])/$', MsgConsumer.as_asgi(), name='messages'),
]
