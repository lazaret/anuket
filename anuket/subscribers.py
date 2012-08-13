# -*- coding: utf-8 -*-
""" Pyramid event subscribers."""
import logging
from pyramid.events import BeforeRender, NewRequest
from pyramid.httpexceptions import HTTPForbidden
from pyramid import i18n
from pyramid.security import forget
from formencode import api as formencode_api

from anuket.lib.i18n import MessageFactory


log = logging.getLogger(__name__)


def includeme(config):
    """ Configure the event subscribers.

    :param config: a ``pyramid.config.Configurator`` object
    """
    config.add_subscriber(add_renderer_globals, BeforeRender)
    config.add_subscriber(add_localizer, NewRequest)
    config.add_subscriber(add_csrf_validation, NewRequest)


def add_renderer_globals(event):
    """ Renderers globals event subscriber.

    Add globals to the renderer. Add `_`, `localizer` and `brand_name`
    globals.

    :param event: a ``pyramid.event.BeforeRender`` object
    """
    request = event.get('request')
    # add globals for i18n
    event['_'] = request.translate
    event['localizer'] = request.localizer
    # add application globals from the config file
    settings = request.registry.settings
    event['brand_name'] = settings['anuket.brand_name']


def add_localizer(event):
    """ Localization event subscriber.

    Automaticaly translate strings in the templates.

    :param event: a ``pyramid.event.NewRequest`` object
    """
    def auto_translate(string):
        """ Use the message factory to translate strings."""
        return localizer.translate(MessageFactory(string))

    def gettext_translate(string):
        """ Translate untranslated strings with FormEncode."""
        # Try default translation first
        translation = localizer.old_translate(i18n.TranslationString(string))
        if translation == string:
            # translation failed then use FormEncode
            translation = formencode_api._stdtrans(string)
        return translation

    request = event.request
    localizer = i18n.get_localizer(request)
    request.localizer = localizer
    request.translate = auto_translate

    if not hasattr(localizer, "old_translate"):
        localizer.old_translate = localizer.translate
    locale_name = i18n.get_locale_name(request)
    formencode_api.set_stdtranslation(languages=[locale_name])
    localizer.translate = gettext_translate


def add_csrf_validation(event):
    """ CSRF validation event subscriber.

    If the POST forms do not have a CSRF token, or an invalid one then user is
    logged out and the forbident view is called.

    :param event: a ``pyramid.event.NewRequest`` object
    :raise HTTPForbidden: if the CSRF token is None or invalid
    """
    if event.request.method == 'POST':
        token = event.request.POST.get('_csrf')
        if token is None or token != event.request.session.get_csrf_token():
            headers = forget(event.request)  # force a log out
            raise HTTPForbidden('CSRF token is missing or invalid',
                                headers=headers)
