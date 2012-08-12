# -*- coding: utf-8 -*-
""" Tests for the event subscribers."""
from pyramid import testing

from anuket.tests import AnuketTestCase


class DummyEvent(object):
    """ Empty testing event."""
    pass


class SubscribersTests(AnuketTestCase):
    """ Test the events subscribers."""
    def setUp(self):
        super(SubscribersTests, self).setUp()
        self.config = testing.setUp()

    def tearDown(self):
        super(SubscribersTests, self).tearDown()
        testing.tearDown()

    def test_renderer_globals(self):
        """ Test the `renderer_globals` event subscriber."""
        from anuket.subscribers import add_renderer_globals
        # set up dummy request and dummy event
        request = testing.DummyRequest()
        request.translate = None
        request.localizer = None
        event = {'request': request}
        # merge settings
        request.registry.settings.update(self.settings)
        # test than the rendered globals are added
        add_renderer_globals(event)
        self.assertIn('_', event)
        self.assertIn('localizer', event)
        self.assertIn('brand_name', event)

    def test_add_localizer(self):
        """ Test the `add_localizer` event subscriber."""
        from pyramid.i18n import Localizer
        from anuket.subscribers import add_localizer
        # set up dummy request and dummy event
        event = DummyEvent()
        request = testing.DummyRequest()
        event.request = request
        # test than the localizer is added
        add_localizer(event)
        self.assertIsInstance(request.localizer, Localizer)
        # test than there is auto-translation ('en' is the default language)
        self.assertEqual(request.translate(u'string'), u'string')

    def test_csrf_validation(self):
        """ Test the `csrf_validation` event subscriber."""
        from pyramid.httpexceptions import HTTPForbidden
        from anuket.subscribers import add_csrf_validation
        # set up dummy request and dummy event
        request = testing.DummyRequest()
        event = DummyEvent()
        event.request = request
        event.request.method = 'POST'
        # test than missing token is forbiden
        self.assertRaises(HTTPForbidden, add_csrf_validation, event)
        # test than wrong token is forbiden
        request.params['_csrf'] = 'wrongtoken'
        self.assertRaises(HTTPForbidden, add_csrf_validation, event)
        # test than good token is allowed
        request.params['_csrf'] = event.request.session.get_csrf_token()
        self.assertEqual(add_csrf_validation(event), None)
