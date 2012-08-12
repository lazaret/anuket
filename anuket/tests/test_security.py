# -*- coding: utf-8 -*-
""" Tests for the authentification utilities."""
from pyramid import testing

from anuket.tests import AnuketTestCase


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
