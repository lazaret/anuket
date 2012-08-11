# -*- coding: utf-8 -*-
""" Define a message factory and a locale negotiator."""
from pyramid.i18n import TranslationStringFactory


MessageFactory = TranslationStringFactory('anuket')


def locale_negotiator(request):
    """ Return a locale name by looking at the ``Accept-Language`` HTTP header.

    :param request: a ``pyramid.request`` object
    :return: the language code
    """
    settings = request.registry.settings
    available_languages = settings['pyramid.available_languages'].split()
    return request.accept_language.best_match(available_languages)
