# -*- coding: utf-8 -*-
from unittest import TestCase
from formencode import Invalid
from formencode import validators

from anuket.tests import AnuketTestCase


class ValidatorsUnitTests(TestCase):
    """ Unit tests for the validators library."""

    def test_FirstNameString(self):
        """ Test the FirstNameString validator."""
        from anuket.lib.validators import FirstNameString
        firstname = FirstNameString()
        # test than the validator is a formencode validators.String
        self.assertIsInstance(firstname, validators.String)
        # tests than excesives inner spaces are removed
        self.assertTrue(firstname.to_python("First   name"), "First name")
        # test than string is capitalized
        self.assertTrue(firstname.to_python("firstname"), "Firstname")

    def test_LastNameString(self):
        """ Test the LastNameString validator."""
        from anuket.lib.validators import LastNameString
        lastname = LastNameString()
        # test than the validator is a formencode validators.String
        self.assertIsInstance(lastname, validators.String)
        # test than there is no case change
        self.assertEqual(lastname.to_python("de Fleur"), "de Fleur")

    def test_UsernamePlainText(self):
        """ Test the UsernamePlainText validator."""
        from anuket.lib.validators import UsernamePlainText
        username = UsernamePlainText()
        # test than the validator is a formencode validators.PlainText
        self.assertIsInstance(username, validators.PlainText)
        # tests than all spaces are removed
        self.assertTrue(username.to_python(" user   name "), "username")
        # test than string is lowercased
        self.assertTrue(username.to_python("UsErNaMe"), "username")

    def test_SecurePassword(self):
        """ Test the SecurePassword validator."""
        from anuket.lib.validators import SecurePassword
        password = SecurePassword()
        # test than the validator is a formencode validators.String
        self.assertIsInstance(password, validators.String)
        # test than unsecure password are not accepted
        self.assertRaises(Invalid, password.validate_python, "PassW0rd", None)


class ValidatorsFynctionalTests(AnuketTestCase):
    """ Functional tests for the validators library."""

    def setUp(self):
        super(ValidatorsFynctionalTests, self).setUp()

    def tearDown(self):
        super(ValidatorsFynctionalTests, self).tearDown()

    def test_UniqueAuthUsername(self):
        """ Test the UniqueAuthUsername validator."""
        self.dummy_user_fixture()
        from anuket.lib.validators import UniqueAuthUsername
        username = UniqueAuthUsername()
        # test than duplicate username is not accepted
        values = {'username': u'username'}
        self.assertRaises(Invalid, username.validate_python, values, None)

    def test_UniqueAuthEmail(self):
        """ Test the UniqueAuthEmail validator."""
        self.dummy_user_fixture()
        from anuket.lib.validators import UniqueAuthEmail
        email = UniqueAuthEmail()
        # test than duplicate email are not accepted
        values = {'email': u'email@email.com'}
        self.assertRaises(Invalid, email.validate_python, values, None)
