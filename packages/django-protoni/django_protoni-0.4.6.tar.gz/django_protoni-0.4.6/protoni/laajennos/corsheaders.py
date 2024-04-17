# -*- coding: utf-8 -*-

__jalkeen__ = ('whitenoise', )

import corsheaders
del corsheaders

INSTALLED_APPS.append('corsheaders')

for i, valike in enumerate(MIDDLEWARE):
  if valike in (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
  ):
    break
else:
  i = len(MIDDLEWARE)
MIDDLEWARE.insert(i, 'corsheaders.middleware.CorsMiddleware')
