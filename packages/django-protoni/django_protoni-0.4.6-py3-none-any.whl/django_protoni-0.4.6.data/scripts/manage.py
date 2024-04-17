#!python

import os
import sys


def main():
  # pylint: disable=not-an-iterable
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'protoni.palvelin')
  try:
    import django
  except ImportError as exc:
    raise ImportError(
      "Couldn't import Django. Are you sure it's installed and "
      "available on your PYTHONPATH environment variable? Did you "
      "forget to activate a virtual environment?"
    ) from exc

  django.setup()
  from django.core.management.commands.runserver import Command
  Command.default_addr, Command.default_port = getattr(
    django.conf.settings,
    'RUNSERVER',
    ('127.0.0.1', 8000)
  )
  Command.oletus_ssl_keyfile = getattr(
    django.conf.settings,
    'RUNSERVER_SSL_KEYFILE',
    None
  )
  Command.oletus_ssl_certfile = getattr(
    django.conf.settings,
    'RUNSERVER_SSL_CERTFILE',
    None
  )
  from django.core.management import execute_from_command_line
  execute_from_command_line(sys.argv)


if __name__ == '__main__':
  main()
