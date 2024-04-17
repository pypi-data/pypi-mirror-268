# -*- coding: utf-8 -*-

from importlib.metadata import entry_points
import sys
import warnings

from django.apps import apps
from django.conf import settings
from django.urls import include, path

from django_hosts import patterns, host


_entry_points = (
  # Ks. https://docs.python.org/3/library/importlib.metadata.html#entry-points.
  entry_points
  if sys.version_info >= (3, 10)
  else lambda *, group: entry_points().get(group, ())
)


_yleinen_osoitteisto = []
for entry_point in _entry_points(group='django.nakymat'):
  try:
    moduuli = entry_point.load()
  except (ImportError, AttributeError):
    pass
  else:
    _yleinen_osoitteisto.append(
      path(entry_point.name + '/', include(moduuli)),
    )
    # else
  # for entry_point in _entry_points

# Luo projektiosoitteiston (`osoitteet.py`) mukainen oletuspalvelin.
palvelimet = [
]

# Käy kukin rekisteröity palvelinnimiavaruus läpi.
for entry_point in _entry_points(group='django.palvelin'):
  # Poimi palvelimen nimi ja osoitteistomoduuli.
  nimi, moduuli = entry_point.name, entry_point.value

  # Käytetään osoitteiston nimiavaruutena sovelluksen nimeä.
  sovellus = apps.get_containing_app_config(moduuli)
  if sovellus is None:
    warnings.warn(f'Sovellusta ei löydy: {moduuli!r}', stacklevel=2)
    continue

  # Muodosta palvelinkohtainen osoitteisto yhdistelmänä seuraavista:
  # - nimetty, yksittäinen osoiteavaruus ja
  # - projektitasoiset, yleiset osoiteavaruudet.
  class PalvelinkohtainenOsoitteisto:
    urlpatterns = [
      path(
        '',
        include((moduuli, sovellus.name), namespace=sovellus.name),
      ),
      *_yleinen_osoitteisto
    ]
    # class PalvelinkohtainenOsoitteisto

  # Luo oma moduulinsa tästä osoitteistosta.
  moduuli += '.palvelin'
  sys.modules[moduuli] = PalvelinkohtainenOsoitteisto

  # Muodosta `<palvelin>.*`-määritys, joka hakee käyttämänsä
  # osoitteiston edellä asetetusta luettelosta.
  palvelimet.append(host(rf'^(.*[.])?{nimi}[.].*', moduuli, name=nimi))
  # for entry_point in _entry_points

if not any(palvelin.name == '<oletus>' for palvelin in palvelimet):
  palvelimet.append(
    host(r'', settings.ROOT_URLCONF, name='<oletus>'),
  )

host_patterns = patterns('', *palvelimet)
