# -*- coding: utf-8 -*-
""" Tests for the translation library."""
from pyramid import testing

from anuket.tests import AnuketTestCase
from anuket.tests import AnuketDummyRequest


class I18nTests(AnuketTestCase):
    """ Tests for the i18n library."""
    def setUp(self):
        super(I18nTests, self).setUp()
        self.config = testing.setUp()

    def tearDown(self):
        super(I18nTests, self).tearDown()
        testing.tearDown()

    def test_locale_negotiator(self):
        """ Test the `locale_negociator` function."""
        from anuket.lib.i18n import locale_negotiator

        request = AnuketDummyRequest()
        request.registry.settings.update(self.settings)
        locale = locale_negotiator(request)
        # test the default locale
        self.assertEqual(locale, 'en')
