# -*- coding: utf-8 -*-
import unittest
from pyramid import testing


def _initTestingDB():
    from wepwawet.models import DBSession, Base, AuthUser
    from sqlalchemy import create_engine
    engine = create_engine('sqlite:///:memory:')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    return DBSession


class ViewRootTests(unittest.TestCase):
    def setUp(self):
        self.DBSession = _initTestingDB()
        self.config = testing.setUp()
        # register the `root` routes
        self.config.include('wepwawet.views.root')

    def tearDown(self):
        self.DBSession.remove()
        testing.tearDown()


    def test_01_routes(self):
        """ Test the routes of the `root` views."""
        request = testing.DummyRequest()
        self.assertEqual(request.route_path('home'), '/')
        self.assertEqual(request.route_path('about'), '/about')
        self.assertEqual(request.route_path('login'), '/login')
        self.assertEqual(request.route_path('logout'), '/logout')

    def test_02_root_view(self):
        """ Test the response of the `root_view`."""
        from wepwawet.views.root import root_view
        request = testing.DummyRequest()
        response = root_view(request)
        self.assertEqual(response, {})

        #TODO: add tests for 404 -> functional

    def test_03_forbiden_view_non_logged(self):
        """ Test the response of the `forbiden_view` for non-logged users."""
        from wepwawet.views.root import forbiden_view
        request = testing.DummyRequest(auth_user=None)
        response = forbiden_view(request)
        self.assertEqual(response.location, '/login')

    def test_04_forbiden_view(self):
        """ Test the response of the `forbiden_view` for logged users."""
        from wepwawet.views.root import forbiden_view
        request = testing.DummyRequest(auth_user='test_user')
        response = forbiden_view(request)
        self.assertEqual(response.location, '/')

    def test_05_login_view_non_logged(self):
        """ Test the response of the `login_view` for non-logged users."""
        from wepwawet.views.root import login_view
        request = testing.DummyRequest()
        response = login_view(request)
        self.assertIsNotNone(response['renderer'])

    def test_06_login_view_good_credentials(self):
        """ Test the response of the `login_view` with good credentials."""
        from wepwawet.views.root import login_view
        from wepwawet.models import AuthUser
        user = AuthUser(username=u'test_user', password=u'test_pass')
        self.DBSession.add(user)
        request = testing.DummyRequest()
        request.params['form_submitted'] = u''
        request.params['username'] = u'test_user'
        request.params['password'] = u'test_pass'
        response = login_view(request)
        self.assertEqual(response.location, '/')
        #TODO test fail because of csrf

    def test_07_login_view_bad_credentials(self):
        """ Test the response of the `login_view` with bad credentials."""
        from wepwawet.views.root import login_view
        from wepwawet.models import AuthUser
        user = AuthUser(username=u'test_user', password=u'test_pass')
        self.DBSession.add(user)
        request = testing.DummyRequest()
        request.params['form_submitted'] = u''
        request.params['username'] = u'bad_user'
        request.params['password'] = u'bad_pass'
        response = login_view(request)
        self.assertIsNotNone(response['renderer'])

    def test_08_logout_view(self):
        """ Test the response of the `logout_view`."""
        from wepwawet.views.root import logout_view
        request = testing.DummyRequest()
        response = logout_view(request)
        self.assertEqual(response.location, '/')


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
        _initTestingDB()

    def tearDown(self):
        del self.testapp
        from wepwawet.models import DBSession
        DBSession.remove()


    def test_09_root(self):
        response = self.testapp.get('/')
        self.assertEqual(response.status, '200 OK')

    def test_10_unexisting_page(self):
        response = self.testapp.get('/Some404Page')
        self.assertEqual(response.status, '200 OK')
        self.assertTrue('404' in response.body)

    def test_11_logout(self):
        response = self.testapp.get('/logout')
        self.assertEqual(response.status, '302 Found')
