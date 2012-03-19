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
        from webhelpers.paginate import Page
        self.assertIsInstance(response['users'], Page)

    def test_03_user_list_with_search(self):
        """ Test the response of the `user_list` view with a search."""
        self.auth_user_fixture()
        from wepwawet.views.user import user_list_view
        request = testing.DummyRequest()
        request.method = 'POST'
        request.params['search'] = u'user'
        response = user_list_view(request)
        from webhelpers.paginate import Page
        self.assertIsInstance(response['users'], Page)

    def test_04_user_add(self):
        """ Test the response of the `user_add` view."""
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

    def test_05_not_validate_user_add(self):
        """ Test the response of the `user_add` view not validated."""
        self.auth_user_fixture()
        from wepwawet.views.user import user_add_view
        request = testing.DummyRequest()
        request.matchdict = {'user_id': 1}
        request.method = 'POST' #required for form.validate()
        request.params['form_submitted'] = u''
        response = user_add_view(request)
        from pyramid_simpleform.renderers import FormRenderer
        self.assertIsInstance(response['renderer'], FormRenderer)

    def test_06_user_edit(self):
        """ Test the response of the `user_edit` view."""
        self.auth_user_fixture()
        from wepwawet.views.user import user_edit_view
        request = testing.DummyRequest()
        request.matchdict = {'user_id': 1}
        request.method = 'POST' #required for form.validate()
        request.params['form_submitted'] = u''
        request.params['username'] = u'username'
        request.params['first_name'] = u'firstname'
        request.params['last_name'] = u'lastname'
        request.params['email'] = u'email@email.com'
        request.params['password'] = u'password'
        request.params['password_confirm'] = u'password'
        response = user_edit_view(request)
        self.assertEqual(response.location, '/tools/user')
        self.assertEqual(request.session.pop_flash('success')[0],
                         u"User updated successfully.")

    def test_07_not_validate_user_edit(self):
        """ Test the response of the `user_edit` view not validated."""
        self.auth_user_fixture()
        from wepwawet.views.user import user_edit_view
        request = testing.DummyRequest()
        request.matchdict = {'user_id': 1}
        request.method = 'POST' #required for form.validate()
        request.params['form_submitted'] = u''
        response = user_edit_view(request)
        from pyramid_simpleform.renderers import FormRenderer
        self.assertIsInstance(response['renderer'], FormRenderer)

    def test_08_not_exist_user_edit(self):
        """ Test the response of the `user_edit` view with a non existent
        `user_id`.
        """
        self.auth_user_fixture()
        from wepwawet.views.user import user_edit_view
        request = testing.DummyRequest()
        request.matchdict = {'user_id': 0}
        response = user_edit_view(request)
        self.assertEqual(response.location, '/tools/user')
        self.assertEqual(request.session.pop_flash('error')[0],
                         u"This user did not exist!")

    def test_09_user_delete(self):
        """ Test the response of the `user_delete` view."""
        self.auth_user_fixture()
        from wepwawet.views.user import user_delete_view
        request = testing.DummyRequest()
        request.matchdict = {'user_id': 1}
        response = user_delete_view(request)
        self.assertEqual(response.location, '/tools/user')
        self.assertEqual(request.session.pop_flash('warning')[0],
                         u"User deleted.")

    def test_10_not_exist_user_delete(self):
        """ Test the response of the `user_delete` view with a non existent
        `user_id`.
        """
        self.auth_user_fixture()
        from wepwawet.views.user import user_delete_view
        request = testing.DummyRequest()
        request.matchdict = {'user_id': 0}
        response = user_delete_view(request)
        self.assertEqual(response.location, '/tools/user')
        self.assertEqual(request.session.pop_flash('error')[0],
                         u"This user did not exist!")


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

