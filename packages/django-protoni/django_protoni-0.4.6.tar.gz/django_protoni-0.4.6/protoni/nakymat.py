# -*- coding: utf-8 -*-

from django.conf import settings
from django import forms
from django.shortcuts import redirect
from django.urls import include, path


if 'django.contrib.auth' in settings.INSTALLED_APPS:
  from django.contrib.auth.views import LoginView, LogoutView
  class Sisaankirjautumislomake(LoginView.form_class):
    tallenna_istunto = forms.BooleanField(required=False)
  class Sisaankirjautumisnakyma(LoginView):
    form_class = Sisaankirjautumislomake
    def get_template_names(self):
      return (
        'kirjaudu-sisaan.html',
        'admin/login.html',  # django.contrib.admin
      )
    def form_invalid(self, form):
      if referer := self.request.headers.get('Referer'):
        return redirect(referer)
      return super().form_invalid(form)
      # def form_invalid
    def form_valid(self, form):
      paluu = super().form_valid(form)
      if not form.cleaned_data.get('tallenna_istunto', False):
        self.request.session.set_expiry(0)
      return paluu
      # def form_valid
    # class Sisaankirjautumisnakyma
  class Kirjautuminen:
    urlpatterns = [
      path(
        'sisaan/',
        Sisaankirjautumisnakyma.as_view(),
        name='kirjaudu-sisaan',
      ),
      path('ulos/', LogoutView.as_view(), name='kirjaudu-ulos'),
    ]
    # class Kirjautuminen
  # if 'django.contrib.auth' in settings.INSTALLED_APPS


if 'django.contrib.admin' in settings.INSTALLED_APPS:
  from django.contrib import admin
  class Kanta:
    urlpatterns = [path('', admin.site.urls)]


if 'debug_toolbar' in settings.INSTALLED_APPS:
  class DebugToolbar:
    # Käännetään debug_toolbar-paketin osoitteisto 'djdt`-nimiavaruuteen.
    osoitteet = include('debug_toolbar.urls', namespace='')
    app_name = 'djdt'
    urlpatterns = [
      path('', (osoitteet[0], None, None)),
    ]
