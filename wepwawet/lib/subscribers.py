# -*- coding: utf-8 -*-
from pyramid.events import BeforeRender, NewRequest
from pyramid.i18n import get_localizer, TranslationStringFactory


def includeme(config):
    """Configure subscribers."""
    config.add_subscriber(add_renderer_globals, BeforeRender)
    config.add_subscriber(add_localizer, NewRequest)
    config.add_subscriber(csrf_validation, NewRequest)

def add_renderer_globals(event):
    request = event.get('request')
    event['_'] = request.translate
    event['localizer'] = request.localizer

tsf = TranslationStringFactory('wepwawet')

def add_localizer(event):
    request = event.request
    localizer = get_localizer(request)
    def auto_translate(string):
        return localizer.translate(tsf(string))
    request.localizer = localizer
    request.translate = auto_translate


def csrf_validation(event):
    if event.request.method == "POST":
        token = event.request.POST.get("csrf_token")
        if token is None or token != event.request.session.get_csrf_token():
            raise HTTPForbidden('CSRF token is missing or invalid')
