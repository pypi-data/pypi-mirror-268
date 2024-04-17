# -*- coding: utf-8 -*-

import whitenoise
del whitenoise

if CONFIG('WHITENOISE_RUNSERVER', cast=bool, default=False):
  INSTALLED_APPS.insert(
    0, 'whitenoise.runserver_nostatic'
  )
  MIDDLEWARE[1:1] = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
  ]

STATICFILES_STORAGE = (
  'whitenoise.storage'
  '.CompressedManifestStaticFilesStorage'
)
