# -*- coding: utf-8 -*-
""" Test for the `root` views."""
from pyramid import testing

from anuket.tests import AnuketTestCase
from anuket.tests import AnuketFunctionalTestCase
from anuket.tests import AnuketDummyRequest


class ViewRootTests(AnuketTestCase):
    """ Integration tests for the `root` views."""
    def setUp(self):
        super(ViewRootTests, self).setUp()
        self.config = testing.setUp()
        # register the `root` routes
        self.config.include('anuket.views.root')

    def tearDown(self):
        super(ViewRootTests, self).tearDown()
        testing.tearDown()

    def test_root_routes(self):
        """ Test the routes of the `root` views."""
        request = AnuketDummyRequest()
        self.assertEqual(request.route_path('home'), '/')
        self.assertEqual(request.route_path('about'), '/about')
        self.assertEqual(request.route_path('login'), '/login')
        self.assertEqual(request.route_path('logout'), '/logout')

    def test_root_view(self):
        """ Test the response of the `root_view`."""
        from anuket.views.root import root_view
        request = AnuketDummyRequest()
        response = root_view(request)
        self.assertEqual(response, {})

    def test_forbiden_view_non_logged(self):
        """ Test the response of the `forbiden_view` for non-logged users."""
        from anuket.views.root import forbiden_view
        request = AnuketDummyRequest(auth_user=None)
        response = forbiden_view(request)
        self.assertEqual(response.location, '/login')
        self.assertEqual(request.session.pop_flash('error')[0],
                         u'You are not connected.')

    def test_forbiden_view_logged(self):
        """ Test the response of the `forbiden_view` for logged users."""
        from anuket.views.root import forbiden_view
        request = AnuketDummyRequest(auth_user='test_user')
        response = forbiden_view(request)
        self.assertEqual(response.location, '/')
        self.assertEqual(request.session.pop_flash('error')[0],
                         u'Insufficient permissions!')

    def test_login_view_non_logged(self):
        """ Test the response of the `login_view` for non-logged users."""
        from anuket.views.root import login_view
        request = AnuketDummyRequest()
        response = login_view(request)
        self.assertIsNotNone(response['renderer'])
        # no flash message yet for non-logged users
        self.assertEqual(len(request.session.pop_flash('info')), 0)
        self.assertEqual(len(request.session.pop_flash('error')), 0)

    def test_login_view_valid_credentials(self):
        """ Test the response of the `login_view` with valid credentials."""
        # no crsf_token check because the suscribers are not activated
        from anuket.views.root import login_view
        self.dummy_user_fixture()
        request = AnuketDummyRequest()
        request.method = 'POST'  # required for form.validate()
        request.params['form_submitted'] = u''
        request.params['username'] = u'username'
        request.params['password'] = u'password'
        response = login_view(request)
        self.assertEqual(response.location, '/')
        self.assertEqual(request.session.pop_flash('success')[0],
                         u"Successful login.")

    def test_login_view_wrong_credentials(self):
        """ Test the response of the `login_view` with wrong credentials."""
        # no crsf_token check because the suscribers are not activated
        from anuket.views.root import login_view
        self.dummy_user_fixture()
        request = AnuketDummyRequest()
        request.method = 'POST'  # required for form.validate()
        request.params['form_submitted'] = u''
        request.params['username'] = u'wrong_user'
        request.params['password'] = u'wrong_pass'
        response = login_view(request)
        self.assertIsNotNone(response['renderer'])
        self.assertEqual(request.session.pop_flash('error')[0],
                        u"Check your login credentials!")

    def test_logout_view(self):
        """ Test the response of the `logout_view`."""
        from anuket.views.root import logout_view
        request = AnuketDummyRequest()
        response = logout_view(request)
        self.assertEqual(response.location, '/')
        self.assertEqual(request.session.pop_flash('info')[0],
                        u"You have been disconnected.")


class ViewRootFunctionalTests(AnuketFunctionalTestCase):
    """ Functional tests for the `root` view."""

    def test_home_page(self):
        """ Test the home page response for everybody."""
        response = self.testapp.get('/', status=200)
        self.assertTrue('<title>Home' in response.body.replace('\n', ''))

    def test_about_page(self):
        """ Test the about page response for everybody."""
        response = self.testapp.get('/about', status=200)
        self.assertTrue('<title>About' in response.body.replace('\n', ''))

    def test_unexisting_page(self):
        """ Test the 404 error page response for everybody."""
        response = self.testapp.get('/Some404Page')
        # the status is 200 because managed by @notfound_view_config
        self.assertEqual(response.status, '200 OK')
        self.assertTrue('<title>404' in response.body.replace('\n', ''))
        response.mustcontain('404', 'Page not found!')

    def test_login_page_non_loged(self):
        """ Test the login page response for everybody."""
        response = self.testapp.get('/login', status=200)
        self.assertTrue('<title>Login' in response.body.replace('\n', ''))

    def test_login_page_valid_credentials(self):
        """ Test login with valid user credentials."""
        response = self.connect_dummy_user_fixture()

        self.assertEqual(response.status, '302 Found')
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/')
        self.assertTrue('Successful login.' in redirect.body)

    def test_login_page_wrong_credentials(self):
        """ Test login with wrong credentials."""
        response = self.testapp.get('/login', status=200)
        csrf_token = response.form.fields['_csrf'][0].value
        params = {
            'form_submitted': u'',
            '_csrf': csrf_token,
            'username': u'wrong_user',
            'password': u'wrong_pass',
            'submit': True}
        response = self.testapp.post('/login', params, status=200)
        self.assertTrue('Check your login credentials!'
                        in response.body)

    def test_login_without_csrf_token(self):
        """ Test login without a csrf token."""
        params = {
            'form_submitted': u'',
            'submit': True}
        response = self.testapp.post('/login', params, status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/login')
        self.assertTrue('You are not connected.' in redirect.body)

    def test_logout(self):
        """ Test the logout response."""
        response = self.testapp.get('/logout', status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/')
        self.assertTrue('You have been disconnected' in redirect.body)
