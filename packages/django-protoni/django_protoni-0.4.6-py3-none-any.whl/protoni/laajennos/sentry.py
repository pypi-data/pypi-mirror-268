# -*- coding: utf-8 -*-

'''
Sentry-SDK-käyttöönotto. Edellyttää seuraavien muuttujien määrityksen:
- SENTRY_DSN: Sentry-palvelimen yhteysosoite
- SENTRY_PAKETTIVERSIO: sen Pip-paketin nimi, jonka versionumero
  ilmoitetaan Sentrylle.
'''
import logging

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration
from sentry_sdk.scrubber import EventScrubber, DEFAULT_DENYLIST

# Poimi DSN-yhteysosoite.
try:
  dsn = CONFIG('SENTRY_DSN')
except UndefinedValueError:
  raise ImportError

# Poimi sen paketin nimi, jonka versionumero ilmoitetaan Sentrylle.
try:
  paketti = CONFIG('SENTRY_PAKETTIVERSIO')
except UndefinedValueError:
  del dsn
  raise ImportError

# Poimi paketin versionumero.
from importlib.metadata import PackageNotFoundError, version
try:
  versio = version(paketti)
except PackageNotFoundError:
  del dsn
  raise ImportError
finally:
  del paketti
  del PackageNotFoundError, version

# Asetetaan Sentry ohittamaan SSL-varmenteen tarkistus,
# mikäli tätä vastaava parametri on asetettu.
if CONFIG('SENTRY_OHITA_VARMENNE', cast=bool, default=False):
  sentry_sdk.transport.HttpTransport._get_pool_options \
  = lambda self, ca_certs: {
    'num_pools': 2,
    'cert_reqs': 'CERT_NONE',
  }

# Alusta Sentry-määritys.
# Ks. https://docs.sentry.io/platforms/python/guides/django/
sentry_sdk.init(
  dsn=dsn,
  release=versio,
  integrations=[
    LoggingIntegration(
      level=logging.INFO,
      event_level=logging.WARNING,
    ),
    DjangoIntegration(),
  ],
  send_default_pii=CONFIG(
    'SENTRY_SEND_DEFAULT_PII',
    cast=bool,
    default=False,
  ),
  event_scrubber=EventScrubber(
    denylist=[
      *DEFAULT_DENYLIST,
      *CONFIG(
        'SENTRY_DENYLIST',
        cast=lambda x: filter(None, x.split(',')),
        default='',
      ),
    ],
  ),
)
del logging
del sentry_sdk, DjangoIntegration, LoggingIntegration
del EventScrubber, DEFAULT_DENYLIST
del dsn, versio
