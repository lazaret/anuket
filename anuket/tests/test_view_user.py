# -*- coding: utf-8 -*-
""" Test for the `user` views."""
from pyramid import testing

from anuket.tests import AnuketTestCase
from anuket.tests import AnuketFunctionalTestCase
from anuket.tests import AnuketDummyRequest


class ViewUserTests(AnuketTestCase):
    """ Integration tests for the `user` views."""
    def setUp(self):
        super(ViewUserTests, self).setUp()
        self.config = testing.setUp()
        # register the `tools` routes
        self.config.include('anuket.views.user')

    def tearDown(self):
        super(ViewUserTests, self).tearDown()
        testing.tearDown()

    def test_user_routes(self):
        """ Test the route of the `user` view."""
        request = AnuketDummyRequest()
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

    def test_user_list_view(self):
        """ Test the response of the `user_list` view."""
        self.dummy_user_fixture()
        from anuket.views.user import user_list_view
        request = AnuketDummyRequest()
        response = user_list_view(request)
        from webhelpers.paginate import Page
        self.assertIsInstance(response['users'], Page)

    def test_user_list_view_with_search(self):
        """ Test the response of the `user_list` view with a search."""
        self.dummy_user_fixture()
        from anuket.views.user import user_list_view
        request = AnuketDummyRequest()
        request.method = 'POST'
        request.params['search'] = u'user'
        response = user_list_view(request)
        from webhelpers.paginate import Page
        self.assertIsInstance(response['users'], Page)

    def test_user_list_view_with_empty_search(self):
        """ Test the response of the `user_list` view with a search who have an
        empty result.
        """
        self.dummy_user_fixture()
        from anuket.views.user import user_list_view
        request = AnuketDummyRequest()
        request.method = 'POST'
        request.params['search'] = u'donotfoundme'
        response = user_list_view(request)
        from webhelpers.paginate import Page
        self.assertIsInstance(response['users'], Page)
        self.assertEqual(request.session.pop_flash('error')[0],
                         u"There is no results!")

    def test_user_list_view_with_sort(self):
        """ Test the response of the `user_list` view with a column sort."""
        self.dummy_user_fixture()
        from anuket.views.user import user_list_view
        request = AnuketDummyRequest()
        request.method = 'POST'
        request.params['sort'] = 'username'
        response = user_list_view(request)
        from webhelpers.paginate import Page
        self.assertIsInstance(response['users'], Page)

    def test_user_add_view(self):
        """ Test the response of the `user_add` view."""
        self.dummy_group_fixture()
        password = self.password_fixture()
        from anuket.views.user import user_add_view
        request = AnuketDummyRequest()
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
                         u"User added.")

    def test_user_add_view_not_validated(self):
        """ Test the response of the `user_add` view not validated."""
        from anuket.views.user import user_add_view
        request = AnuketDummyRequest()
        request.method = 'POST'  # required for form.validate()
        request.params['form_submitted'] = u''
        response = user_add_view(request)
        from pyramid_simpleform.renderers import FormRenderer
        self.assertIsInstance(response['renderer'], FormRenderer)

    def test_user_edit_view(self):
        """ Test the response of the `user_edit` view."""
        self.dummy_user_fixture()
        from anuket.views.user import user_edit_view
        request = AnuketDummyRequest()
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
                         u"User updated.")

    def test_user_edit_view_not_validated(self):
        """ Test the response of the `user_edit` view not validated."""
        self.dummy_user_fixture()
        from anuket.views.user import user_edit_view
        request = AnuketDummyRequest()
        request.matchdict = {'user_id': 1}
        request.method = 'POST'  # required for form.validate()
        request.params['form_submitted'] = u''
        response = user_edit_view(request)
        from pyramid_simpleform.renderers import FormRenderer
        self.assertIsInstance(response['renderer'], FormRenderer)

    def test_user_edit_view_not_exist(self):
        """ Test the response of the `user_edit` view with a non existent
        `user_id`.
        """
        self.dummy_user_fixture()
        from anuket.views.user import user_edit_view
        request = AnuketDummyRequest()
        request.matchdict = {'user_id': 0}
        response = user_edit_view(request)
        self.assertEqual(response.location, '/tools/user')
        self.assertEqual(request.session.pop_flash('error')[0],
                         u"This user did not exist!")

    def test_user_show_view(self):
        """ Test the response of the `user_show` view."""
        self.dummy_user_fixture()
        from anuket.views.user import user_show_view
        request = AnuketDummyRequest()
        request.matchdict = {'user_id': 1}
        response = user_show_view(request)
        from anuket.models.auth import AuthUser
        user = AuthUser.get_by_id(1)
        self.assertIsInstance(response['user'], AuthUser)
        self.assertEqual(response['user'], user)

    def test_user_show_view_not_exist(self):
        """ Test the response of the `user_show` view with a non existent
        `user_id`.
        """
        self.dummy_user_fixture()
        from anuket.views.user import user_show_view
        request = AnuketDummyRequest()
        request.matchdict = {'user_id': 0}
        response = user_show_view(request)
        self.assertEqual(response.location, '/tools/user')
        self.assertEqual(request.session.pop_flash('error')[0],
                         u"This user did not exist!")

    def test_user_delete_view(self):
        """ Test the response of the `user_delete` view."""
        self.dummy_user_fixture()
        from anuket.views.user import user_delete_view
        request = AnuketDummyRequest()
        request.matchdict = {'user_id': 1}
        request.referer = '/tools/user'
        response = user_delete_view(request)
        self.assertEqual(response.location, '/tools/user')
        self.assertEqual(request.session.pop_flash('warn')[0],
                         u"User deleted.")

    def test_user_delete_view_not_exist(self):
        """ Test the response of the `user_delete` view with a non existent
        `user_id`.
        """
        self.dummy_user_fixture()
        from anuket.views.user import user_delete_view
        request = AnuketDummyRequest()
        request.matchdict = {'user_id': 0}
        request.referer = '/tools/user'
        response = user_delete_view(request)
        self.assertEqual(response.location, '/tools/user')
        self.assertEqual(request.session.pop_flash('error')[0],
                         u"This user did not exist!")

    def test_user_delete_view_without_referer_is_forbiden(self):
        """ test the response of the `user_delete` view wile trying to
        directly delete an user (with no referer).
        """
        self.config.include('anuket.views.root')  # register the `root` routes
        self.dummy_user_fixture()
        from anuket.views.user import user_delete_view
        request = AnuketDummyRequest()
        request.matchdict = {'user_id': 1}
        request.referer = None
        response = user_delete_view(request)
        self.assertEqual(response.location, '/')
        self.assertEqual(request.session.pop_flash('error')[0],
                         u"Insufficient permissions!")

    def test_user_delete_view_of_only_admin_is_forbiden(self):
        """ Test the response of the `user_delete` view wile trying to
        delete the only admin user.
        """
        self.admin_user_fixture()
        from anuket.views.user import user_delete_view
        request = AnuketDummyRequest()
        request.matchdict = {'user_id': 1}
        request.referer = '/tools/user'
        response = user_delete_view(request)
        self.assertEqual(response.location, '/tools/user')
        self.assertEqual(request.session.pop_flash('error')[0],
                         u"Deletion of the only admin forbidden!")

    def test_password_edit_view(self):
        """ Test the response of the `password_edit` view."""
        self.dummy_user_fixture()
        password = self.password_fixture()
        from anuket.views.user import password_edit_view
        request = AnuketDummyRequest()
        request.matchdict = {'user_id': 1}
        request.method = 'POST'  # required for form.validate()
        request.params['form_submitted'] = u''
        request.params['user_id'] = 1
        request.params['password'] = password
        request.params['password_confirm'] = password
        response = password_edit_view(request)
        self.assertEqual(response.location, '/tools/user')
        self.assertEqual(request.session.pop_flash('success')[0],
                         u"Password updated.")

    def test_password_edit_view_not_validated(self):
        """ Test the response of the `password_edit` view not validated."""
        self.dummy_user_fixture()
        from anuket.views.user import password_edit_view
        request = AnuketDummyRequest()
        request.matchdict = {'user_id': 1}
        request.method = 'POST'  # required for form.validate()
        request.params['form_submitted'] = u''
        response = password_edit_view(request)
        from pyramid_simpleform.renderers import FormRenderer
        self.assertIsInstance(response['renderer'], FormRenderer)

    def test_password_edit_view_not_exist(self):
        """ Test the response of the `password_edit` view with a non
        existent `user_id`.
        """
        self.dummy_user_fixture()
        from anuket.views.user import password_edit_view
        request = AnuketDummyRequest()
        request.matchdict = {'user_id': 0}
        response = password_edit_view(request)
        self.assertEqual(response.location, '/tools/user')
        self.assertEqual(request.session.pop_flash('error')[0],
                         u"This user did not exist!")


class ViewUserFunctionalTests(AnuketFunctionalTestCase):
    """ Functional tests for the `user` views."""

    def test_user_list_page_for_admin(self):
        """ Test the user list page with admin credentials."""
        response = self.connect_admin_user_fixture()

        response = self.testapp.get('/tools/user', status=200)
        self.assertEqual(response.request.path, '/tools/user')
        self.assertTrue('<title>User list' in response.body.replace('\n', ''))

    def test_user_list_page_is_forbiden_for_non_admin(self):
        """ Test than the user list page is forbiden for non admin users."""
        response = self.connect_dummy_user_fixture()

        response = self.testapp.get('/tools', status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/')
        self.assertTrue('Insufficient permissions!' in redirect.body)

    def test_user_list_page_is_forbiden_for_anonymous(self):
        """ Test than the user list page is forbiden for non logged users."""
        response = self.testapp.get('/tools/user', status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/login')
        self.assertTrue('You are not connected.' in redirect.body)

    def test_user_add_page_for_admin(self):
        """ Test the add user form with admin credentials."""
        group = self.dummy_group_fixture()
        password = self.password_fixture()
        response = self.connect_admin_user_fixture()

        response = self.testapp.get('/tools/user/add', status=200)
        self.assertEqual(response.request.path, '/tools/user/add')
        self.assertTrue('<title>Add user' in response.body.replace('\n', ''))
        # add a (valid) dummy user with the form
        form = response.form
        form.set('username', 'username')
        form.set('first_name', 'firstname')
        form.set('last_name', 'lastname')
        form.set('email', 'email@email.com')
        form.set('group_id', group.group_id)
        form.set('password', password)
        form.set('password_confirm', password)
        submit = form.submit('form_submitted')
        redirect = submit.follow()
        self.assertEqual(redirect.request.path, '/tools/user')
        self.assertTrue('User added.' in redirect.body)
        self.assertTrue('email@email.com' in redirect.body)

    def test_user_add_page_is_forbiden_for_non_admin(self):
        """ Test than the add user form is forbiden for non admin users."""
        response = self.connect_dummy_user_fixture()

        response = self.testapp.get('/tools/user/add', status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/')
        self.assertTrue('Insufficient permissions!' in redirect.body)

    def test_user_add_page_is_forbiden_for_anonymous(self):
        """ Test than the add user form is forbiden for non logged users."""
        response = self.testapp.get('/tools/user/add', status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/login')
        self.assertTrue('You are not connected.' in redirect.body)

    def test_user_show_page_for_admin(self):
        """ Test the show user page with admin credentials."""
        response = self.connect_admin_user_fixture()

        response = self.testapp.get('/tools/user/1/show', status=200)
        self.assertEqual(response.request.path, '/tools/user/1/show')
        # the set up user is admin himself
        self.assertTrue('admin' in response.body.replace('\n', ''))

    def test_user_show_page_is_forbiden_for_non_admin(self):
        """ Test than the show user page is forbiden for non admin users."""
        response = self.connect_dummy_user_fixture()

        response = self.testapp.get('/tools/user/1/show', status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/')
        self.assertTrue('Insufficient permissions!' in redirect.body)

    def test_user_show_page_is_forbiden_for_anonymous(self):
        """ Test than the show user page is forbiden for non logged users."""
        response = self.testapp.get('/tools/user/1/show', status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/login')
        self.assertTrue('You are not connected.' in redirect.body)

    def test_user_edit_page_for_admin(self):
        """ Test the edit user form with admin credentials."""
        response = self.connect_admin_user_fixture()

        response = self.testapp.get('/tools/user/1/edit', status=200)
        self.assertEqual(response.request.path, '/tools/user/1/edit')
        self.assertTrue('<title>Edit user' in response.body.replace('\n', ''))
        # edit the admin user with the form
        form = response.form
        form.set('username', 'username')
        form.set('first_name', 'firstname')
        form.set('last_name', 'lastname')
        form.set('email', 'email@email.com')
        # we do not change the group
        form.set('group_id', 1)
        submit = form.submit('form_submitted')
        redirect = submit.follow()
        self.assertEqual(redirect.request.path, '/tools/user')
        self.assertTrue('User updated.' in redirect.body)
        self.assertTrue('email@email.com' in redirect.body)

    def test_user_edit_page_for_admin_with_group_change(self):
        """ Test the edit user form of a dummy user with admin credentials."""
        self.dummy_user_fixture()
        response = self.connect_admin_user_fixture()

        response = self.testapp.get('/tools/user/1/edit', status=200)
        self.assertEqual(response.request.path, '/tools/user/1/edit')
        self.assertTrue('<title>Edit user' in response.body.replace('\n', ''))
        # edit the dummy user with the form
        form = response.form
        form.set('username', 'newusername')
        form.set('first_name', 'newfirstname')
        form.set('last_name', 'newlastname')
        form.set('email', 'newemail@email.com')
        # we change the group to the admin group
        form.set('group_id', 2)
        submit = form.submit('form_submitted')
        redirect = submit.follow()
        self.assertEqual(redirect.request.path, '/tools/user')
        self.assertTrue('User updated.' in redirect.body)
        self.assertTrue('newemail@email.com' in redirect.body)

    def test_user_edit_page_is_forbiden_for_non_admin(self):
        """ Test than the edit user form is forbiden for non admin users."""
        response = self.connect_dummy_user_fixture()

        response = self.testapp.get('/tools/user/1/edit', status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/')
        self.assertTrue('Insufficient permissions!' in redirect.body)

    def test_user_edit_page_is_forbiden_for_anonymous(self):
        """ Test than the edit user form is forbiden for non logged users."""
        response = self.testapp.get('/tools/user/1/edit', status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/login')
        self.assertTrue('You are not connected.' in redirect.body)

    def test_direct_user_delete_is_forbiden_for_admin(self):
        """ Test than direct delete is forbiden for admin users."""
        # Even, admins are not allowed to delete an entry by hiting the
        # link in the adresse bar. A referer is requested.
        response = self.connect_admin_user_fixture()

        response = self.testapp.get('/tools/user/1/delete', status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/')
        self.assertTrue('Insufficient permissions!' in redirect.body)

    def test_direct_user_delete_is_forbiden_for_non_admin(self):
        """ Test than direct delete is forbiden for non admin users."""
        response = self.connect_dummy_user_fixture()

        response = self.testapp.get('/tools/user/1/delete', status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/')
        self.assertTrue('Insufficient permissions!' in redirect.body)

    def test_direct_user_delete_is_forbiden_for_anonymous(self):
        """ Test than direct delete is forbiden for non logged users."""
        user = self.dummy_user_fixture()
        response = self.testapp.get('/tools/user/1/delete', status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/login')
        self.assertTrue('You are not connected.'
                        in redirect.body)
        # check than the user is effectively still in the database
        from anuket.models.auth import AuthUser
        usercheck = AuthUser.get_by_id(1)
        self.assertTrue(usercheck, user)

    def test_user_delete_with_referer(self):
        """ Test the delete of an user by an admin user with a referer."""
        self.dummy_user_fixture()  # id=1
        response = self.connect_admin_user_fixture()  # id=2
        response = self.testapp.get(
            '/tools/user/1/delete',
            extra_environ={'HTTP_REFERER': '/tools/user'},
            status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/tools/user')
        self.assertTrue('User deleted.' in redirect.body)
        self.assertFalse('email@email.com' in redirect.body)

    def test_only_admin_delete_with_referer_is_forbiden(self):
        """ Test than it's forbiden to delete the only admin with referer."""
        response = self.connect_admin_user_fixture()  # id=1
        response = self.testapp.get(
            '/tools/user/1/delete',
            extra_environ={'HTTP_REFERER': '/tools/user'},
            status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/tools/user')
        self.assertTrue('Deletion of the only admin forbidden!'
                        in redirect.body)

    def test_password_edit_page_for_admin(self):
        """ Test the edit password form with admin credentials."""
        password = self.password_fixture()
        response = self.connect_admin_user_fixture()

        response = self.testapp.get('/tools/user/1/password', status=200)
        self.assertEqual(response.request.path, '/tools/user/1/password')
        self.assertTrue('<title>Edit password'
                        in response.body.replace('\n', ''))
        # edit the admin user password with the form
        form = response.form
        form.set('password', password)
        form.set('password_confirm', password)
        submit = form.submit('form_submitted')
        redirect = submit.follow()
        self.assertEqual(redirect.request.path, '/tools/user')
        self.assertTrue('Password updated.' in redirect.body)

    def test_password_edit_page_is_forbiden_for_non_admin(self):
        """ Test than edit password form is forbiden for non admin users."""
        response = self.connect_dummy_user_fixture()

        response = self.testapp.get('/tools/user/1/password', status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/')
        self.assertTrue('Insufficient permissions!' in redirect.body)

    def test_password_edit_page_is_forbiden_for_anonymous(self):
        """ Test than edit password form is forbiden for non logged users."""
        response = self.testapp.get('/tools/user/1/password', status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/login')
        self.assertTrue('You are not connected.' in redirect.body)
