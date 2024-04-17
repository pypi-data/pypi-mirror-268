# -*- coding: utf-8 -*-

import django_heroku

django_heroku.settings(locals(), logging=False)

if not isinstance(MIDDLEWARE, list):
  MIDDLEWARE = list(MIDDLEWARE)
