# -*- coding: utf-8 -*-
import unittest
from pyramid import testing


class ViewToolsTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        # register the `tools` routes
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


#    def test_view_fn_forbidden(self):
#        from pyramid.httpexceptions import HTTPForbidden
#        from wepwawet.views.tools import tools_index_view
#        self.config.testing_securitypolicy(userid='hank')
#        request = testing.DummyRequest()
#        request.context = testing.DummyResource()
#        self.assertRaises(HTTPForbidden, tools_index_view, request)
# do not work somewhere -> move to functional tests because @view_config
# need a browser


class FunctionalViewToolsTests(unittest.TestCase):
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


    def test_01_tools_page_is_forbiden(self):
        """ Test than the tools page is forbiden for non logged users."""
        response = self.testapp.get('/tools', status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/login')
        self.assertTrue('You are not connected, please log in.' in redirect.body)

#TODO add test for admin loged users
#TODO add test for non authorised but logged user

#    def test_01_tools(self):
#        response = self.testapp.get('/tools')
#        self.assertEqual(response.status, '200 OK')
#        #TODO: error because need credentials
