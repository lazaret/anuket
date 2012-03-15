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


class ViewUserTests(unittest.TestCase):
    def setUp(self):
        self.DBSession = _initTestingDB()
        self.config = testing.setUp()
        # register the `tools` routes
        self.config.include('wepwawet.views.user')

    def tearDown(self):
        self.DBSession.remove()
        testing.tearDown()

    def test_01_routes(self):
        """ Test the route of the `user` view."""
        request = testing.DummyRequest()
        self.assertEqual(request.route_path('tools.user_list'), '/tools/user')
        self.assertEqual(request.route_path('tools.user_add'), '/tools/user/add')
        self.assertEqual(request.route_path('tools.user_edit', user_id=1), '/tools/user/1/edit')
        self.assertEqual(request.route_path('tools.user_delete', user_id=1), '/tools/user/1/delete')

    def test_02_user_list(self):
        """ Test the response of the `list`."""
        from wepwawet.views.user import user_list_view
        from wepwawet.models import AuthUser
        user = AuthUser(username=u'test_user', password=u'test_pass')
        self.DBSession.add(user)
        request = testing.DummyRequest()
        response = user_list_view(request)
        #TODO add data test
        #self.assertEqual(response, {})

#    def test_03_user_add(self):
#        from wepwawet.views.user import user_add_view
#        request = testing.DummyRequest()
#        response = user_add_view(request)
#        #TODO add db record

#    def test_04_user_edit(self):
#        from wepwawet.views.user import user_edit_view
#        request = testing.DummyRequest()
#        response = user_edit_view(request)
#        #TODO add db record

#    def test_05_user_delete(self):
#        from wepwawet.views.user import user_delete_view
#        request = testing.DummyRequest()
#        response = user_delete_view(request)
#        #TODO add db record



class FunctionalViewUserTests(unittest.TestCase):
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


    def test_01_user_list_page_is_forbiden(self):
        """ Test than the user list page is forbiden for non logged users."""
        response = self.testapp.get('/tools/user', status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/login')
        self.assertTrue('You are not connected, please log in.' in redirect.body)

