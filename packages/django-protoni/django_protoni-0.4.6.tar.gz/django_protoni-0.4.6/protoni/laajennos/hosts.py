# -*- coding: utf-8 -*-

import django_hosts
del django_hosts

INSTALLED_APPS += ['django_hosts']
MIDDLEWARE.insert(
  min((
    i for i, ohjain in enumerate(MIDDLEWARE)
    if ohjain in (
      'django.middleware.gzip.GZipMiddleware',
    )
  ), default=-1) + 1,
  'django_hosts.middleware.HostsRequestMiddleware',
)
MIDDLEWARE.insert(
  len(MIDDLEWARE) + 1,
  'django_hosts.middleware.HostsResponseMiddleware',
)

ROOT_HOSTCONF = 'protoni.palvelimet'
DEFAULT_HOST = CONFIG('DJANGO_DEFAULT_HOST', default='<oletus>')
