# -*- coding: utf-8 -*-
from pyramid.i18n import get_localizer, TranslationStringFactory


def includeme(config):
    """Configure subscribers."""
    config.add_subscriber(add_renderer_globals, 'pyramid.events.BeforeRender')
    config.add_subscriber(add_localizer, 'pyramid.events.NewRequest')

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
