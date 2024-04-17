# -*- coding: utf-8 -*-

from .asetukset import *

DEBUG = True
ALLOWED_HOSTS = CONFIG(
  'ALLOWED_HOSTS',
  cast=lambda x: list(map(str.strip, x.split(','))),
  default='*',
)
SECRET_KEY = 'epäjärjestelmällistyttämättömyydellänsäkäänköhän'
