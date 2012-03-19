# -*- coding: utf-8 -*-
from pyramid import testing

from wepwawet.tests import WepwawetTestCase


class ViewUserTests(WepwawetTestCase):
    def setUp(self):
        super(ViewUserTests, self).setUp()
        self.config = testing.setUp()
        # register the `tools` routes
        self.config.include('wepwawet.views.user')

    def tearDown(self):
        super(ViewUserTests, self).tearDown()
        testing.tearDown()


    def test_01_routes(self):
        """ Test the route of the `user` view."""
        request = testing.DummyRequest()
        self.assertEqual(request.route_path('tools.user_list'), '/tools/user')
        self.assertEqual(request.route_path('tools.user_add'), '/tools/user/add')
        self.assertEqual(request.route_path('tools.user_edit', user_id=1), '/tools/user/1/edit')
        self.assertEqual(request.route_path('tools.user_delete', user_id=1), '/tools/user/1/delete')

    def test_02_user_list(self):
        """ Test the response of the `user_list` view."""
        self.auth_user_fixture()
        from wepwawet.views.user import user_list_view
        request = testing.DummyRequest()
        response = user_list_view(request)
        #TODO add data test
        #self.assertEqual(response, {})

    def test_03_user_add(self):
        """ test the response of the `user_add` view."""
        from wepwawet.views.user import user_add_view
        request = testing.DummyRequest()
        request.method = 'POST' #required for form.validate()
        request.params['form_submitted'] = u''
        request.params['username'] = u'username'
        request.params['first_name'] = u'firstname'
        request.params['last_name'] = u'lastname'
        request.params['email'] = u'email@email.com'
        request.params['password'] = u'password'
        request.params['password_confirm'] = u'password'
        response = user_add_view(request)
        self.assertEqual(response.location, '/tools/user')
        self.assertEqual(request.session.pop_flash('success')[0],
                         u"User added successfully.")

    def test_04_user_edit(self):
        """ test the response of the `user_edit` view."""
        self.auth_user_fixture()
        from wepwawet.views.user import user_edit_view
        request = testing.DummyRequest()
#        response = user_edit_view(request)
        #TODO add db record

    def test_05_user_delete(self):
        """ test the response of the `user_delete` view."""
        self.auth_user_fixture()
        from wepwawet.views.user import user_delete_view
        request = testing.DummyRequest()
#        response = user_delete_view(request)
        #TODO add db record


class FunctionalViewUserTests(WepwawetTestCase):
    def setUp(self):
        super(FunctionalViewUserTests, self).setUp()
        from wepwawet import main
        app = main({}, **self.settings)
        from webtest import TestApp
        self.testapp = TestApp(app)

    def tearDown(self):
        super(FunctionalViewUserTests, self).tearDown()
        del self.testapp


    def test_01_user_list_page_is_forbiden(self):
        """ Test than the user list page is forbiden for non logged users."""
        response = self.testapp.get('/tools/user', status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/login')
        self.assertTrue('You are not connected, please log in.' in redirect.body)

