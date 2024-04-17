# -*- coding: utf-8 -*-

from .asetukset import *


SECRET_KEY = CONFIG('SECRET_KEY', default='subatominen-hiukkanen')

ALLOWED_HOSTS = CONFIG(
  'ALLOWED_HOSTS',
  cast=lambda x: list(map(str.strip, x.split(','))),
)

DEBUG = CONFIG("DEBUG", cast=bool, default=False)

SECURE_CONTENT_TYPE_NOSNIFF = True # per security.W006
SECURE_BROWSER_XSS_FILTER = True # per security.W007
SECURE_SSL_REDIRECT = True # per security.W008
SESSION_COOKIE_SECURE = True # per security.W012
CSRF_COOKIE_SECURE = True # per security.W016
X_FRAME_OPTIONS = 'Deny' # per security.W019

# Ks. Django SSL/HTTPS
# Huom. otsake `X-Forwarded-Proto` asetettava proxy-palvelimella!
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

EMAIL_BACKEND = CONFIG('EMAIL_BACKEND', default=(
  'django.core.mail.backends.smtp.EmailBackend'
))
EMAIL_FILE_PATH = CONFIG('EMAIL_FILE_PATH', default=(
  os.path.join(BASE_DIR, 'sahkoposti')
))
EMAIL_HOST = CONFIG('EMAIL_HOST', default='localhost')
EMAIL_PORT = CONFIG('EMAIL_PORT', default=25, cast=int)

# Käytetään tiivistettä staattisten tiedostojen nimissä,
# mikäli asetus on vakioarvossa.
try:
  STATICFILES_STORAGE
except NameError:
  STATICFILES_STORAGE = (
    'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
  )

# Salasanavaatimukset.
AUTH_PASSWORD_VALIDATORS = [
  {'NAME': (
    'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
  )},
  {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
  {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
  {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
