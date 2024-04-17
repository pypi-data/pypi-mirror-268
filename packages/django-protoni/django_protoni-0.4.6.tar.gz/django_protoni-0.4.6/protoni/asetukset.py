# -*- coding: utf-8 -*-

import importlib
import os
from pathlib import Path
from sys import version_info
import warnings

from decouple_multi import AutoConfig, UndefinedValueError


# Käytetään yhtenäistä entry_point-toteutusta, vaikka Python 3.9 ja 3.10
# eroavat tältä osin toisistaan.
if version_info >= (3, 10):
  from importlib.metadata import entry_points
  def ep_hakemisto(ep):
    # Huomaa, että `entry_point`-standardi ei hyväksy vinoviivoja
    # osana liitospistettä. Korvataan mahdolliset pisteet viivoilla.
    return ep.dist.locate_file(ep.value.replace('.', '/'))

else:
  # Ks. https://docs.python.org/3/library/importlib.metadata.html#entry-points.
  from importlib.metadata import entry_points as _entry_points
  def entry_points(*, group):
    return _entry_points().get(group, ())
  def ep_hakemisto(ep):
    from importlib.metadata import distributions
    ep_value = ep.value.replace('.', '/')
    for distribution in distributions():
      if (hakemisto := distribution.locate_file(ep_value)).exists():
        return hakemisto
    else:
      raise ValueError(f'Tiedostoa ei löydetty: {ep.value}')

  # else (Python < 3.10)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Asetusparametrit.
CONFIG = AutoConfig(
  search_path=tuple(filter(None, (
    # Ympäristössä määritetty hakemisto.
    # Tunnistetaan myös mahdollinen `ENV_POLKU`-muuttuja.
    os.getenv('PROTONI', None) or os.getenv('ENV_POLKU', None),
    # Käytetään toissijaisesti nykyistä työhakemistoa.
    Path().resolve(),
    # Kolmannella sijalla käytetään asennettujen pakettien
    # määrittelemiä `decouple.asetukset`-hakemistoja.
    *(
      ep_hakemisto(entry_point)
      for entry_point in entry_points(
        group='decouple.asetukset'
      )
    ),
    # Huomaa, että `decouple` käyttää näiden lisäksi viimekätisenä
    # hakemistona käsillä olevan moduulin (__file__) sisältävää polkua.
  ))),
)

# IP-osoite ja portti, jossa `manage.py runserver`-palvelinta ajetaan.
# Oletus 127.0.0.1, 8000.
# Osoite ja portti poimitaan pilkulla eroteltuina.
# Mikäli vain toinen on annettu, tulkitaan numeerinen arvo portin
# numeroksi ja muu arvo IP-osoitteeksi.
RUNSERVER = CONFIG(
  'RUNSERVER',
  cast=lambda x: (
    # pylint: disable=undefined-variable
    ('127.0.0.1', 8000) if not x
    else (h_p[0], int(h_p[1])) if ',' in x and (h_p := x.split(','))
    else ('127.0.0.1', int(x)) if x.isdecimal()
    else (x, 8000)
  ),
  default=None,
)

# SSL-avain- ja -varmennetiedosto, joita käytetään https-kehityspalvelimen
# suojaamiseen.
RUNSERVER_SSL_KEYFILE=CONFIG(
  'RUNSERVER_SSL_KEYFILE',
  default=None,
)
RUNSERVER_SSL_CERTFILE=CONFIG(
  'RUNSERVER_SSL_CERTFILE',
  default=None,
)

# Oletusasetukset.
AUTH_PASSWORD_VALIDATORS = []

try:
  DATABASES = {
    'default': {
      'ENGINE': CONFIG('DB_ENGINE'),
    }
  }

except UndefinedValueError:
  pass

else:
  DATABASES['default'].update({
    'django.db.backends.sqlite3': lambda: {
      'NAME': CONFIG('DB_NAME', default=os.path.join(BASE_DIR, 'db.sqlite3')),
    },
    'django.db.backends.mysql': lambda: {
      'HOST': CONFIG('DB_HOST', default='127.0.0.1'),
      'PORT': CONFIG('DB_PORT', default=3306, cast=int),
      'NAME': CONFIG('DB_NAME'),
      'USER': CONFIG('DB_USER'),
      'PASSWORD': CONFIG('DB_PASSWORD', default=''),
      'OPTIONS': {
        'sql_mode': 'TRADITIONAL',
        'charset': 'utf8',
        'init_command': (
          'SET '
          'NAMES "utf8", '
          'sql_mode=STRICT_TRANS_TABLES,'
          'default_storage_engine=INNODB,'
          'character_set_connection=utf8,'
          'character_set_database=utf8,'
          'character_set_server=utf8,'
          'collation_connection=utf8_swedish_ci'
        ),
      },
    },
    'django.db.backends.postgresql': lambda: {
      'HOST': CONFIG('DB_HOST', default='127.0.0.1'),
      'PORT': CONFIG('DB_PORT', default=5432, cast=int),
      'NAME': CONFIG('DB_NAME'),
      'USER': CONFIG('DB_USER'),
      'PASSWORD': CONFIG('DB_PASSWORD', default=''),
    },
  }.get(DATABASES['default']['ENGINE'], lambda: {})())

INSTALLED_APPS = [
  *(
    f'django.contrib.{sovellus}'
    for sovellus in (
      'admin',
      'auth',
      'contenttypes',
      'sessions',
      'messages',
      'staticfiles',
      'humanize',
    )
    if sovellus in CONFIG(
      'DJANGO_SOVELLUKSET',
      cast=lambda x: x.split(','),
      default='',
    )
  ),
  'django.forms',
]
MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  *((
    'django.contrib.sessions.middleware.SessionMiddleware',
  ) if 'django.contrib.sessions' in INSTALLED_APPS else ()),
  'django.middleware.locale.LocaleMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  *((
    'django.contrib.auth.middleware.AuthenticationMiddleware',
  ) if 'django.contrib.auth' in INSTALLED_APPS else ()),
  *((
    'django.contrib.messages.middleware.MessageMiddleware',
  ) if 'django.contrib.messages' in INSTALLED_APPS else ()),
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Käytetään istuntojen tallennukseen tietokantaa, mikäli se on
# määritetty ja muutoin evästeitä.
SESSION_ENGINE = CONFIG(
  'SESSION_ENGINE',
  default=(
    'django.contrib.sessions.backends.db' if 'DATABASES' in locals()
    else 'django.contrib.sessions.backends.signed_cookies'
  )
)

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
      'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        *((
          'django.contrib.auth.context_processors.auth',
        ) if 'django.contrib.auth' in INSTALLED_APPS else ()),
        *((
          'django.contrib.messages.context_processors.messages',
        ) if 'django.contrib.messages' in INSTALLED_APPS else ()),
      ],
    },
  },
]

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

ROOT_URLCONF = 'protoni.osoitteet'
WSGI_APPLICATION = 'protoni.wsgi.application'

LANGUAGE_CODE = 'fi-fi'
TIME_ZONE = CONFIG('TIME_ZONE', default='UTC')
USE_I18N = True
USE_TZ = CONFIG('USE_TZ', cast=bool, default=True)

STATIC_URL = '/static/'
STATIC_ROOT = CONFIG(
  'STATIC_ROOT',
  default=os.path.join('/', 'tmp', 'protoni', 'static')
)

MEDIA_URL = '/media/'
MEDIA_ROOT = CONFIG(
  'MEDIA_ROOT',
  default=os.path.join('/', 'tmp', 'protoni', 'media')
)

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Sisäänkirjautumisosoite.
LOGIN_URL = '/kirjaudu/sisaan/'


LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'formatters': {
    'verbose': {
      'format': ('%(asctime)s [%(process)d] [%(levelname)s] '
            'pathname=%(pathname)s lineno=%(lineno)s '
            'funcname=%(funcName)s %(message)s'),
      'datefmt': '%Y-%m-%d %H:%M:%S'
    },
    'simple': {
      'format': '%(levelname)s %(message)s'
    }
  },
  'handlers': {
    'null': {
      'level': 'DEBUG',
      'class': 'logging.NullHandler',
    },
    'console': {
      'level': 'INFO',
      'class': 'logging.StreamHandler',
      'formatter': 'verbose'
    }
  },
  'loggers': {
    'django': {
      'handlers': ['console'],
      'level': 'DEBUG',
      'propagate': True,
    },
    'django.request': {
      'handlers': ['console'],
      'level': 'DEBUG',
      'propagate': False,
    },
  }
}


# Lataa asennetut sovellukset.
for entry_point in entry_points(group='django.sovellus'):
  INSTALLED_APPS.append(entry_point.value)


# Lataa asennetut asetuslaajennokset.
for entry_point in entry_points(group='django.asetukset'):
  spec = importlib.util.find_spec(entry_point.value)
  if spec is None:
    entry_point.load()
    warnings.warn(f'Virheellinen laajennos: {entry_point!r}')
    continue
  with open(spec.origin, encoding='utf-8') as laajennos_mod:
    # pylint: disable=exec-used
    try: exec(compile(laajennos_mod.read(), spec.origin, 'exec'))
    except ImportError: pass
  # for entry_point in pkg_resources.iter_entry_points
