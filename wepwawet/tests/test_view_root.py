# -*- coding: utf-8 -*-
import unittest
#import transaction
from pyramid import testing

#from wepwawet.models import DBSession



class MyTest(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        # register routes
        self.config.include('wepwawet.views.root')

    def tearDown(self):
        testing.tearDown()


    def test_01_root_view(self):
        from wepwawet.views.root import root_view
        request = testing.DummyRequest()
        response = root_view(request)
        # test routes
        self.assertEqual(request.route_path('home'), '/')
        self.assertEqual(request.route_path('about'), '/about')
        # test response
        self.assertEqual(response, {})
        #TODO: add tests for 404

#    def test_02_forbident_view(self):
#        #TODO: add tests for forbiden
#        pass

    def test_03_login_view_not_logged(self):
        from wepwawet.views.root import login_view
        request = testing.DummyRequest()
        response = login_view(request)
        # test route
        self.assertEqual(request.route_path('login'), '/login')
        # test response
        self.assertIsNotNone(response['renderer'])


    def test_05_logout_view(self):
        from wepwawet.views.root import logout_view
        request = testing.DummyRequest()
        response = logout_view(request)
        # test route
        self.assertEqual(request.route_path('logout'), '/logout')
        # test response
        self.assertEqual(response.location, '/')
        self.assertEqual(response.headers['Content-Length'], '0')
