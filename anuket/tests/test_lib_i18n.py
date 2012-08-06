# -*- coding: utf-8 -*-
from pyramid import testing

from anuket.tests import AnuketTestCase


class DummyRequest(testing.DummyRequest):
    """ Extend the pyramid testing.DummyRequest class with the WebOb
    `accept_language` attribute."""

    from pyramid.request import Request
    accept_language = Request.accept_language


class I18nTests(AnuketTestCase):
    """ Tests for the i18n library."""
    def setUp(self):
        super(I18nTests, self).setUp()
        self.config = testing.setUp()

    def tearDown(self):
        super(I18nTests, self).tearDown()
        testing.tearDown()


    def test_locale_negotiator(self):
        """ Test the `locale_negociator`."""
        from anuket.lib.i18n import locale_negotiator

        request = DummyRequest()
        request.registry.settings.update(self.settings)
        locale = locale_negotiator(request)
        # test the default locale
        self.assertEqual(locale, 'en')
