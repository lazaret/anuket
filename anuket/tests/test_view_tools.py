# -*- coding: utf-8 -*-
""" Test for the `tools` views."""
from pyramid import testing

from anuket.tests import AnuketTestCase
from anuket.tests import AnuketFunctionalTestCase
from anuket.tests import AnuketDummyRequest


class ViewToolsTests(AnuketTestCase):
    """ Integration tests for the `tools` views."""
    def setUp(self):
        super(ViewToolsTests, self).setUp()
        self.config = testing.setUp()
        # register the `tools` routes
        self.config.include('anuket.views.tools')

    def tearDown(self):
        super(ViewToolsTests, self).tearDown()
        testing.tearDown()

    def test_tools_routes(self):
        """ Test the routes of the `tools` view."""
        request = AnuketDummyRequest()
        self.assertEqual(request.route_path('tools.index'), '/tools')

    def test_tools_view(self):
        """ Test the response of the `tools_index_view`."""
        from anuket.views.tools import tools_index_view
        request = AnuketDummyRequest()
        response = tools_index_view(request)
        self.assertEqual(response, {})


class ViewToolsFunctionalTests(AnuketFunctionalTestCase):
    """ Functional tests for the `user` views."""

    def test_tools_page_for_admin(self):
        """ Test the tools page with admin credentials."""
        response = self.connect_admin_user_fixture()

        response = self.testapp.get('/tools', status=200)
        self.assertEqual(response.request.path, '/tools')
        self.assertTrue('<title>Tools' in response.body.replace('\n', ''))

    def test_tools_page_is_forbiden_for_non_admin(self):
        """ Test than the tools page is forbiden for non admin users."""
        response = self.connect_dummy_user_fixture()

        response = self.testapp.get('/tools', status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/')
        self.assertTrue('Insufficient permissions!' in redirect.body)

    def test_tools_page_is_forbiden_for_anonymous(self):
        """ Test than the tools page is forbiden for non logged users."""
        response = self.testapp.get('/tools', status=302)
        redirect = response.follow()
        self.assertEqual(redirect.status, '200 OK')
        self.assertEqual(redirect.request.path, '/login')
        self.assertTrue('You are not connected.' in redirect.body)
