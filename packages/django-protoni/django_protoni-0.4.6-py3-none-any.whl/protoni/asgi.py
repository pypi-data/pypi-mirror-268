# -*- coding: utf-8 -*-

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "protoni.palvelin")


django = get_asgi_application()

try:
  from pistoke.kasittelija import WebsocketKasittelija
except ModuleNotFoundError:
  async def websocket(*args):
    raise NotImplementedError('Pistoke-pakettia ei ole asennettu!')
else:
  websocket = WebsocketKasittelija()


async def application(scope, receive, send):
  if scope['type'] == 'http':
    return await django(scope, receive, send)
  elif scope['type'] == 'websocket':
    return await websocket(scope, receive, send)
  else:
    raise NotImplementedError(f'Tuntematon pyyntö {scope["type"]}')
  # async def application
