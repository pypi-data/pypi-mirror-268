# -*- coding: utf-8 -*-

if not CONFIG('DDT', cast=bool, default=True):
  raise ImportError

import debug_toolbar
del debug_toolbar

INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE.insert(
  min((
    i for i, ohjain in enumerate(MIDDLEWARE)
    if ohjain in (
      'django.middleware.gzip.GZipMiddleware',
    )
  ), default=-1) + 1,
  'debug_toolbar.middleware.DebugToolbarMiddleware'
)
INTERNAL_IPS = ['127.0.0.1', '::1']
