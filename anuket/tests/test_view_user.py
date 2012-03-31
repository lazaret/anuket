# -*- coding: utf-8 -*-
from pyramid import testing

from anuket.tests import AnuketTestCase


class ViewUserTests(AnuketTestCase):
    """ Integration tests for the `user` view."""
    def setUp(self):
        super(ViewUserTests, self).setUp()
        self.config = testing.setUp()
        # register the `tools` routes
        self.config.include('anuket.views.user')

    def tearDown(self):
        super(ViewUserTests, self).tearDown()
        testing.tearDown()

    def test_01_routes(self):
        """ Test the route of the `user` view."""
        request = testing.DummyRequest()
        self.assertEqual(request.route_path('tools.user_list'), '/tools/user')
        self.assertEqual(request.route_path('tools.user_add'),
                         '/tools/user/add')
        self.assertEqual(request.route_path('tools.user_show', user_id=1),
                         '/tools/user/1/show')
        self.assertEqual(request.route_path('tools.user_edit', user_id=1),
                         '/tools/user/1/edit')
        self.assertEqual(request.route_path('tools.user_delete', user_id=1),
                         '/tools/user/1/delete')
        self.assertEqual(request.route_path('tools.password_edit', user_id=1),
                         '/tools/user/1/password')

    def test_02_user_list(self):
        """ Test the response of the `user_list` view."""
        self.auth_user_fixture()
        from anuket.views.user import user_list_view
        request = testing.DummyRequest()
        response = user_list_view(request)
        from webhelpers.paginate import Page
        self.assertIsInstance(response['users'], Page)

    def test_03_user_list_with_search(self):
        """ Test the response of the `user_list` view with a search."""
        self.auth_user_fixture()
        from anuket.views.user import user_list_view
        request = testing.DummyRequest()
        request.method = 'POST'
        request.params['search'] = u'user'
        response = user_list_view(request)
        from webhelpers.paginate import Page
        self.assertIsInstance(response['users'], Page)

    def test_04_user_add(self):
        """ Test the response of the `user_add` view."""
        self.auth_group_fixture()
        password = self.password_fixture()
        from anuket.views.user import user_add_view
        request = testing.DummyRequest()
        request.method = 'POST'  # required for form.validate()
        request.params['form_submitted'] = u''
        request.params['username'] = u'username'
        request.params['first_name'] = u'firstname'
        request.params['last_name'] = u'lastname'
        request.params['email'] = u'email@email.com'
        request.params['group_id'] = 1
        request.params['password'] = password
        request.params['password_confirm'] = password
        response = user_add_view(request)
        self.assertEqual(response.location, '/tools/user')
        self.assertEqual(request.session.pop_flash('success')[0],
                         u"User added successfully.")

    def test_05_not_validate_user_add(self):
        """ Test the response of the `user_add` view not validated."""
        from anuket.views.user import user_add_view
        request = testing.DummyRequest()
        request.method = 'POST'  # required for form.validate()
        request.params['form_submitted'] = u''
        response = user_add_view(request)
        from pyramid_simpleform.renderers import FormRenderer
        self.assertIsInstance(response['renderer'], FormRenderer)

    def test_06_user_edit(self):
        """ Test the response of the `user_edit` view."""
        self.auth_user_fixture()
        from anuket.views.user import user_edit_view
        request = testing.DummyRequest()
        request.matchdict = {'user_id': 1}
        request.method = 'POST'  # required for form.validate()
        request.params['form_submitted'] = u''
        request.params['user_id'] = 1
        request.params['username'] = u'username'
        request.params['first_name'] = u'firstname'
        request.params['last_name'] = u'lastname'
        request.params['email'] = u'email@email.com'
        request.params['group_id'] = 1
        response = user_edit_view(request)
        self.assertEqual(response.location, '/tools/user')
        self.assertEqual(request.session.pop_flash('success')[0],
                         u"User updated successfully.")

    def test_07_not_validate_user_edit(self):
        """ Test the response of the `user_edit` view not validated."""
        self.auth_user_fixture()
        from anuket.views.user import user_edit_view
        request = testing.DummyRequest()
        request.matchdict = {'user_id': 1}
        request.method = 'POST'  # required for form.validate()
        request.params['form_submitted'] = u''
        response = user_edit_view(request)
        from pyramid_simpleform.renderers import FormRenderer
        self.assertIsInstance(response['renderer'], FormRenderer)

    def test_08_not_exist_user_edit(self):
        """ Test the response of the `user_edit` view with a non existent
        `user_id`.
        """
        self.auth_user_fixture()
        from anuket.views.user import user_edit_view
        request = testing.DummyRequest()
        request.matchdict = {'user_id': 0}
        response = user_edit_view(request)
        self.assertEqual(response.location, '/tools/user')
        self.assertEqual(request.session.pop_flash('error')[0],
                         u"This user did not exist!")

    def test_09_user_show(self):
        """ Test the response of the `user_show` view."""
        self.auth_user_fixture()
        from anuket.views.user import user_show_view
        request = testing.DummyRequest()
        request.matchdict = {'user_id': 1}
        response = user_show_view(request)
        from anuket.models import AuthUser
        user = AuthUser.get_by_id(1)
        self.assertIsInstance(response['user'], AuthUser)
        self.assertEqual(response['user'], user)

    def test_10_not_exist_user_show(self):
        """ Test the response of the `user_show` view with a non existent
        `user_id`.
        """
        self.auth_user_fixture()
        from anuket.views.user import user_show_view
        request = testing.DummyRequest()
        request.matchdict = {'user_id': 0}
        response = user_show_view(request)
        self.assertEqual(response.location, '/tools/user')
        self.assertEqual(request.session.pop_flash('error')[0],
                         u"This user did not exist!")

    def test_11_user_delete(self):
        """ Test the response of the `user_delete` view."""
        self.auth_user_fixture()
        from anuket.views.user import user_delete_view
        request = testing.DummyRequest()
        request.matchdict = {'user_id': 1}
        response = user_delete_view(request)
        self.assertEqual(response.location, '/tools/user')
        self.assertEqual(request.session.pop_flash('warning')[0],
                         u"User deleted.")

    def test_12_not_exist_user_delete(self):
        """ Test the response of the `user_delete` view with a non existent
        `user_id`.
        """
        self.auth_user_fixture()
        from anuket.views.user import user_delete_view
        request = testing.DummyRequest()
        request.matchdict = {'user_id': 0}
        response = user_delete_view(request)
        self.assertEqual(response.location, '/tools/user')
        self.assertEqual(request.session.pop_flash('error')[0],
                         u"This user did not exist!")

    def test_13_password_edit(self):
        """ Test the response of the `password_edit_view` view."""
        self.auth_user_fixture()
        password = self.password_fixture()
        from anuket.views.user import password_edit_view
        request = testing.DummyRequest()
        request.matchdict = {'user_id': 1}
#        request.method = 'POST'  # required for form.validate()
#        request.params['form_submitted'] = u''
#        request.params['user_id'] = 1
#        request.params['password'] = password
#        request.params['password_confirm'] = password
#        response = password_edit_view(request)
#        self.assertEqual(response.location, '/tools/user')
#        self.assertEqual(request.session.pop_flash('success')[0],
#                         u"Password updated successfully.")
#TODO check the validation process seems than there is an unecessary unique
#user check

    def test_14_not_exist_password_edit(self):
        """ Test the response of the `password_edit_view` view with a non
        existent `user_id`.
        """
        self.auth_user_fixture()
        from anuket.views.user import password_edit_view
        request = testing.DummyRequest()
        request.matchdict = {'user_id': 0}
        response = password_edit_view(request)
        self.assertEqual(response.location, '/tools/user')
        self.assertEqual(request.session.pop_flash('error')[0],
                         u"This user did not exist!")

#TODO: tests for sorted user list
#TODO: non-validate tests for unsecure pass, user/mail not unique


class FunctionalViewUserTests(AnuketTestCase):
    """ Functional tests for the `user` view."""
    def setUp(self):
        super(FunctionalViewUserTests, self).setUp()
        from anuket import main
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
        self.assertTrue('You are not connected, please log in.'
                        in redirect.body)



#    def test_02_user_list_page_is_forbiden_for_non_admin(self):
#        """ Test than the user list page is forbiden for non admin users."""
#        pass
#TODO add a forbiden test for logged non-admin


    def test_03_user_list_page_for_admin(self):
        """ Test the user list page with admin credentials."""

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
        # realy tests the user list
        response = self.testapp.get('/tools/user', status=200)
        self.assertEqual(response.request.path, '/tools/user')
        self.assertTrue('<title>User list' in response.body.replace('\n', ''))
#TODO add a fixture to connect admin



    def test_04_user_add_page_is_forbiden(self):
        """ Test than the add user form is forbiden for non logged users."""
        response = self.testapp.get('/tools/user/add', status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/login')
        self.assertTrue('You are not connected, please log in.'
                        in redirect.body)

    def test_05_user_show_page_is_forbiden(self):
        """ Test than the show user page is forbiden for non logged users."""
        self.auth_user_fixture()
        response = self.testapp.get('/tools/user/1/show', status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/login')
        self.assertTrue('You are not connected, please log in.'
                        in redirect.body)

    def test_06_user_edit_page_is_forbiden(self):
        """ Test than the edit user form is forbiden for non logged users."""
        self.auth_user_fixture()
        response = self.testapp.get('/tools/user/1/edit', status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/login')
        self.assertTrue('You are not connected, please log in.'
                        in redirect.body)

    def test_07_user_delete_is_forbiden(self):
        """ Test than deleting an user is forbiden for non logged users."""
        self.auth_user_fixture()
        response = self.testapp.get('/tools/user/1/delete', status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/login')
        self.assertTrue('You are not connected, please log in.'
                        in redirect.body)
        #TODO add a db check than the user is not deleted

    def test_08_password_edit_page_is_forbiden(self):
        """ Test than password change page is forbiden for non logged users."""
        self.auth_user_fixture()
        response = self.testapp.get('/tools/user/1/password', status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/login')
        self.assertTrue('You are not connected, please log in.'
                        in redirect.body)
