# -*- coding: utf-8 -*-
import unittest
from pyramid import testing


class ViewRootTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        # register the `root` routes
        self.config.include('wepwawet.views.tools')

    def tearDown(self):
        testing.tearDown()

    def test_01_routes(self):
        """ Test the route of the `tools` view."""
        request = testing.DummyRequest()
        self.assertEqual(request.route_path('tools.index'), '/tools')

    def test_02_tools_view(self):
        """ Test the response of the `tools_index_view`."""
        from wepwawet.views.tools import tools_index_view
        request = testing.DummyRequest()
        response = tools_index_view(request)
        self.assertEqual(response, {})


class FunctionalViewRootTests(unittest.TestCase):
    def setUp(self):
        from wepwawet import main
        settings = { 'sqlalchemy.url': 'sqlite:///:memory:',
                    'pyramid.available_languages': 'en',
                    'wepwawet.brand_name': 'Wepwawet',
                    'mako.directories': 'wepwawet:templates'}
        app = main({}, **settings)
        from webtest import TestApp
        self.testapp = TestApp(app)

    def tearDown(self):
        del self.testapp

#    def test_03_tools(self):
#        response = self.testapp.get('/tools')
#        self.assertEqual(response.status, '200 OK')
#        #TODO: error because need credentials
