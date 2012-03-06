# -*- coding: utf-8 -*-
from pyramid.events import BeforeRender, NewRequest
from pyramid.httpexceptions import HTTPForbidden
from pyramid.i18n import get_localizer, TranslationStringFactory


def includeme(config):
    """Configure subscribers."""
    config.add_subscriber(add_renderer_globals, BeforeRender)
    config.add_subscriber(add_localizer, NewRequest)
    config.add_subscriber(csrf_validation, NewRequest)


def add_renderer_globals(event):
    request = event.get('request')
    # add globals for i18n
    event['_'] = request.translate
    event['localizer'] = request.localizer
    # add application globals from the config file
    settings = request.registry.settings
    event['brand_name'] = settings['wepwawet.brand_name']

def add_localizer(event):
    tsf = TranslationStringFactory('wepwawet')
    request = event.request
    localizer = get_localizer(request)
    def auto_translate(string):
        return localizer.translate(tsf(string))
    request.localizer = localizer
    request.translate = auto_translate

def csrf_validation(event):
    if event.request.method == 'POST':
        token = event.request.POST.get('_csrf')
        if token is None or token != event.request.session.get_csrf_token():
            raise HTTPForbidden('CSRF token is missing or invalid')
