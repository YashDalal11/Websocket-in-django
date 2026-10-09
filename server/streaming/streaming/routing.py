from django.urls import path
from ..chat import consumers

websocket_urlpatterns = [
    path('ws/socket-server/',consumers.ChatConsumer.as_asgi())
]

from channels.routing import ProtocolTypeRouter, URLRouter
from my_proj.game.routing import websockets
application = ProtocolTypeRouter({
    "websocket": [
    path('ws/socket-server/',consumers.ChatConsumer.as_asgi())
],
})