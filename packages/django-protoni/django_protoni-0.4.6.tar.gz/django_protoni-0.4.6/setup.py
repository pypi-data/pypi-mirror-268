# -* - coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
  setup_requires='git-versiointi>=1.6rc3',
  name='django-protoni',
  packages=find_packages(),
  py_modules=['manage'],
  include_package_data=True,
  scripts=['manage.py'],
  install_requires=['Django', 'python-decouple-multi'],
  entry_points={
    'django.nakymat': [
      '__debug__ = protoni.nakymat:DebugToolbar',
      'kirjaudu = protoni.nakymat:Kirjautuminen',
      'kanta = protoni.nakymat:Kanta',
    ],
    'django.asetukset': [
      'celery = protoni.laajennos.celery',
      'corsheaders = protoni.laajennos.corsheaders',
      'debug_toolbar = protoni.laajennos.debug_toolbar',
      'dj_database_url = protoni.laajennos.dj_database_url',
      'extensions = protoni.laajennos.extensions',
      'heroku = protoni.laajennos.heroku',
      'hosts = protoni.laajennos.hosts',
      'pipeline = protoni.laajennos.pipeline',
      'sentry = protoni.laajennos.sentry',
      'whitenoise = protoni.laajennos.whitenoise',
    ],
  },
)
