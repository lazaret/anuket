# -*- coding: utf-8 -*-
from pyramid import testing

from anuket.tests import AnuketTestCase


class ViewToolsTests(AnuketTestCase):
    """ Integration tests for the `tools` view."""
    def setUp(self):
        super(ViewToolsTests, self).setUp()
        self.config = testing.setUp()
        # register the `tools` routes
        self.config.include('anuket.views.tools')

    def tearDown(self):
        super(ViewToolsTests, self).tearDown()
        testing.tearDown()

    def test_01_routes(self):
        """ Test the route of the `tools` view."""
        request = testing.DummyRequest()
        self.assertEqual(request.route_path('tools.index'), '/tools')

    def test_02_tools_view(self):
        """ Test the response of the `tools_index_view`."""
        from anuket.views.tools import tools_index_view
        request = testing.DummyRequest()
        response = tools_index_view(request)
        self.assertEqual(response, {})


class FunctionalViewToolsTests(AnuketTestCase):
    """ Functional tests for the `user` view."""
    def setUp(self):
        super(FunctionalViewToolsTests, self).setUp()
        from anuket import main
        app = main({}, **self.settings)
        from webtest import TestApp
        self.testapp = TestApp(app)

    def tearDown(self):
        super(FunctionalViewToolsTests, self).tearDown()
        del self.testapp

    def test_01_tools_page_is_forbiden(self):
        """ Test than the tools page is forbiden for non logged users."""
        response = self.testapp.get('/tools', status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/login')
        self.assertTrue('You are not connected, please log in.'
                        in redirect.body)

    def test_02_tools_page_is_forbiden_for_non_admin(self):
        """ Test than the tools page is forbiden for non admin users."""
        # connect dummy user
        self.auth_user_fixture()
        response = self.testapp.get('/login', status=200)
        csrf_token = response.form.fields['_csrf'][0].value
        params = {
            'form_submitted': u'',
            '_csrf': csrf_token,
            'username': u'username',
            'password': u'password',
            'submit': True}
        response = self.testapp.post('/login', params, status=302)
        # realy test the tools page
        response = self.testapp.get('/tools', status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/')
        self.assertTrue('You do not have the permission to do this!'
                        in redirect.body)

    def test_03_tools_page_for_admin(self):
        """ Test the tools page with admin credentials."""
        # connect admin user
        self.admin_user_fixture()
        response = self.testapp.get('/login', status=200)
        csrf_token = response.form.fields['_csrf'][0].value
        params = {
            'form_submitted': u'',
            '_csrf': csrf_token,
            'username': u'admin',
            'password': u'admin',
            'submit': True}
        response = self.testapp.post('/login', params, status=302)
        # realy test the tools page
        response = self.testapp.get('/tools', status=200)
        self.assertEqual(response.request.path, '/tools')
        self.assertTrue('<title>Tools' in response.body.replace('\n', ''))


#TODO add a fixture for loggin dummy user and admin


