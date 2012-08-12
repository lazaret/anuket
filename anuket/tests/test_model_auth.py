# -*- coding: utf-8 -*-
""" Tests for the Authentification related models."""
import datetime

from anuket.tests import AnuketTestCase


class ModelAuthUserTests(AnuketTestCase):
    """ Tests for the ``AuthUser`` model class."""

    def test_AuthUser_columns(self):
        """ Test the ``AuthUser`` model class columns and types."""
        self.dummy_user_fixture()
        from anuket.models.auth import AuthUser
        user = self.DBSession.query(AuthUser).filter_by().first()
        self.assertIsInstance(user.user_id, int)
        self.assertIsInstance(user.username, unicode)
        self.assertIsInstance(user.first_name, unicode)
        self.assertIsInstance(user.last_name, unicode)
        self.assertIsInstance(user.email, unicode)
        self.assertIsInstance(user.password, unicode)
        self.assertIsInstance(user.created, datetime.date)

    def test_AuthUser_username_unique_constraint(self):
        """ Test `username` uniqueness in the ``AuthUser`` model class."""
        self.dummy_user_fixture()
        from anuket.models.auth import AuthUser
        from sqlalchemy.exc import IntegrityError
        duplicate = AuthUser(username=u'username')
        self.DBSession.add(duplicate)
        self.assertRaises(IntegrityError, self.DBSession.flush)

    def test_AuthUser_group_relation(self):
        """ Test the relationship with the ``AuthGroup`` model class."""
        self.dummy_user_fixture()
        from anuket.models.auth import AuthUser
        user = self.DBSession.query(AuthUser).filter_by().first()
        self.assertIsInstance(user.group_id, int)
        self.assertTrue(user.group)

    def test_AuthUser_get_by_id(self):
        """ Test the `get_by_id` method of the ``AuthUser`` model class."""
        user = self.dummy_user_fixture()
        from anuket.models.auth import AuthUser
        self.assertTrue(AuthUser.get_by_id(1))
        self.assertEqual(user, AuthUser.get_by_id(1))

    def test_AuthUser_get_by_username(self):
        """ Test the `get_by_username` method of the ``AuthUser`` model class.
        """
        user = self.dummy_user_fixture()
        from anuket.models.auth import AuthUser
        self.assertTrue(AuthUser.get_by_username(u'username'))
        self.assertEqual(user, AuthUser.get_by_username(u'username'))

    def test_AuthUser_get_by_email(self):
        """ Test the `get_by_email` method of the ``AuthUser`` model class."""
        user = self.dummy_user_fixture()
        from anuket.models.auth import AuthUser
        self.assertTrue(AuthUser.get_by_email(u'email@email.com'))
        self.assertEqual(user, AuthUser.get_by_email(u'email@email.com'))

    def test_AuthUser_crypted_password(self):
        """ Test than the recorded password is crypted in the database."""
        user = self.dummy_user_fixture()
        self.assertNotEqual(user._password, u'password')

    def test_AuthUser_check_password(self):
        """ Test the `check_password` method of the ``AuthUser`` model class.
        """
        self.dummy_user_fixture()
        from anuket.models.auth import AuthUser
        self.assertTrue(AuthUser.check_password(u'username', u'password'))
        self.assertFalse(AuthUser.check_password(u'username', u'wrongpass'))
        self.assertFalse(AuthUser.check_password(u'nobody', u'password'))


class ModelAuthGroupTests(AnuketTestCase):
    """ Tests for the ``AuthGroup`` model class."""

    def test_AuthGroup_columns(self):
        """ Test the ``AuthGroup`` model class columns and types."""
        self.dummy_group_fixture()
        from anuket.models.auth import AuthGroup
        group = self.DBSession.query(AuthGroup).filter_by().first()
        self.assertIsInstance(group.group_id, int)
        self.assertIsInstance(group.groupname, unicode)

    def test_AuthGroup_groupname_unique_constraint(self):
        """ Test `groupname` uniqueness in the ``AuthGroup`` model class."""
        self.dummy_group_fixture()
        from anuket.models.auth import AuthGroup
        from sqlalchemy.exc import IntegrityError
        duplicate = AuthGroup(groupname=u'groupname')
        self.DBSession.add(duplicate)
        self.assertRaises(IntegrityError, self.DBSession.flush)

    def test_AuthGroup_get_by_id(self):
        """ Test the `get_by_id` method of the ``AuthGroup`` model class."""
        group = self.dummy_group_fixture()
        from anuket.models.auth import AuthGroup
        self.assertTrue(AuthGroup.get_by_id(1))
        self.assertEqual(group, AuthGroup.get_by_id(1))
