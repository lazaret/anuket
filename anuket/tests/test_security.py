# -*- coding: utf-8 -*-
""" Tests for the authentification utilities."""
from pyramid import testing

from anuket.tests import AnuketTestCase
from anuket.tests import AnuketDummyRequest


class DummyAuthenticationPolicy:
    """ Dummy a uthentication policy class for testing Anuket
    authentification.
    """
    def __init__(self, result):
        self.result = result

    def unauthenticated_userid(self, request):
        """ Fake the `pyramid.security.unauthenticated_userid` method."""
        return self.result


class SecurityTests(AnuketTestCase):
    """ Test the authentification utilities."""
    def test_groupfinder(self):
        """ Test the `groupfinder` callback."""
        user = self.dummy_user_fixture()
        from anuket.security import groupfinder
        request = testing.DummyRequest()
        # test with a valid user_id
        groupname = groupfinder(1, request)
        self.assertEqual(groupname, [('group:%s' % user.group.groupname)])
        # test with a wrong username
        groupname = groupfinder(u'wrongname', request)
        self.assertEqual(groupname, None)
        # test with an empty username
        groupname = groupfinder(None, request)
        self.assertEqual(groupname, None)

    def test_get_auth_user(self):
        """ Test the `get_auth_user` function."""
        user = self.dummy_user_fixture()
        from anuket.security import get_auth_user
        request = AnuketDummyRequest()

        from pyramid.interfaces import IAuthenticationPolicy
        policy = DummyAuthenticationPolicy(user.user_id)
        request.registry.registerUtility(policy, IAuthenticationPolicy)

        auth_user = get_auth_user(request)
        self.assertEqual(auth_user, user)
