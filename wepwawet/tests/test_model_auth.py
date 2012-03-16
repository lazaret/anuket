# -*- coding: utf-8 -*-
import datetime

from wepwawet.tests import ModelsTestCase


class ModelAuthUserTests(ModelsTestCase):
    """Tests for the `AuthUser` model class."""

    def test_01_columns(self):
        """ Test the `AuthUser` model class columns and types."""
        self.auth_user_fixture()
        from wepwawet.models import AuthUser
        user = self.DBSession.query(AuthUser).filter_by().first()
        self.assertIsInstance(user.user_id, int)
        self.assertIsInstance(user.username, unicode)
        self.assertIsInstance(user.first_name, unicode)
        self.assertIsInstance(user.last_name, unicode)
        self.assertIsInstance(user.email, unicode)
        self.assertIsInstance(user.password, unicode)
        self.assertIsInstance(user.created, datetime.date)

    def test_02_username_unique_constraint(self):
        """ Test `username` uniqueness in the `AuthUser` model class."""
        self.auth_user_fixture()
        from wepwawet.models import AuthUser
        from sqlalchemy.exc import IntegrityError
        duplicate = AuthUser(username=u'username')
        self.DBSession.add(duplicate)
        self.assertRaises(IntegrityError, self.DBSession.flush)

    def test_03_group_relation(self):
        """ Test the relationship with the `AuthGroup` model class."""
        self.auth_user_fixture()
        from wepwawet.models import AuthUser
        user = self.DBSession.query(AuthUser).filter_by().first()
        self.assertIsInstance(user.group_id, int)
        self.assertTrue(user.group)

    def test_04_get_by_id(self):
        """ Test the `get_by_id` method of the `AuthUser` model class."""
        user = self.auth_user_fixture()
        from wepwawet.models import AuthUser
        self.assertTrue(AuthUser.get_by_id(1))
        self.assertEqual(user, AuthUser.get_by_id(1))

    def test_05_get_by_username(self):
        """ Test the `get_by_username` method of the `AuthUser` model class."""
        user = self.auth_user_fixture()
        from wepwawet.models import AuthUser
        self.assertTrue(AuthUser.get_by_username(u'username'))
        self.assertEqual(user, AuthUser.get_by_username(u'username'))

    def test_06_crypted_password(self):
        """ Test than the recorded password is crypted in the database."""
        user = self.auth_user_fixture()
        from wepwawet.models import AuthUser
        self.assertNotEqual(user._password, u'password')

    def test_07_check_password(self):
        """ Test the `check_password` method of the `AuthUser` model class."""
        self.auth_user_fixture()
        from wepwawet.models import AuthUser
        self.assertTrue(AuthUser.check_password(u'username', u'password'))
        self.assertFalse(AuthUser.check_password(u'username', u'wrongpass'))
        self.assertFalse(AuthUser.check_password(u'nobody', u'password'))


class ModelAuthGroupTests(ModelsTestCase):
    """Tests for the `AuthGroup` model class."""

    def test_01_columns(self):
        """ Test the `AuthGroup` model class columns and types."""
        self.auth_group_fixture()
        from wepwawet.models import AuthGroup
        group = self.DBSession.query(AuthGroup).filter_by().first()
        self.assertIsInstance(group.group_id, int)
        self.assertIsInstance(group.groupname, unicode)

    def test_02_groupname_unique_constraint(self):
        """ Test `groupname` uniqueness in the `AuthGroup` model class."""
        self.auth_group_fixture()
        from wepwawet.models import AuthGroup
        from sqlalchemy.exc import IntegrityError
        duplicate = AuthGroup(groupname=u'groupname')
        self.DBSession.add(duplicate)
        self.assertRaises(IntegrityError, self.DBSession.flush)

    def test_03_get_by_id(self):
        """ Test the `get_by_id` method of the `AuthGroup` model class."""
        group = self.auth_group_fixture()
        from wepwawet.models import AuthGroup
        self.assertTrue(AuthGroup.get_by_id(1))
        self.assertEqual(group, AuthGroup.get_by_id(1))
