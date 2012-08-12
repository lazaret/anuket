# -*- coding: utf-8 -*-
""" tests for the form validation library."""
from formencode import Invalid
from formencode import validators

from anuket.tests import AnuketTestCase


class ValidatorsTests(AnuketTestCase):
    """ Tests the validators library."""

    def test_FirstNameString(self):
        """ Test the ``FirstNameString`` validator."""
        from anuket.lib.validators import FirstNameString
        firstname = FirstNameString()
        # test than the validator is a formencode validators.String
        self.assertIsInstance(firstname, validators.String)
        # tests than excesives inner spaces are removed
        self.assertTrue(firstname.to_python("First   name"), "First name")
        # test than string is capitalized
        self.assertTrue(firstname.to_python("firstname"), "Firstname")

    def test_LastNameString(self):
        """ Test the ``LastNameString`` validator."""
        from anuket.lib.validators import LastNameString
        lastname = LastNameString()
        # test than the validator is a formencode validators.String
        self.assertIsInstance(lastname, validators.String)
        # test than there is no case change
        self.assertEqual(lastname.to_python("de Fleur"), "de Fleur")

    def test_UsernamePlainText(self):
        """ Test the ``UsernamePlainText`` validator."""
        from anuket.lib.validators import UsernamePlainText
        username = UsernamePlainText()
        # test than the validator is a formencode validators.PlainText
        self.assertIsInstance(username, validators.PlainText)
        # tests than all spaces are removed
        self.assertTrue(username.to_python(" user   name "), "username")
        # test than string is lowercased
        self.assertTrue(username.to_python("UsErNaMe"), "username")

    def test_SecurePassword(self):
        """ Test the ``SecurePassword`` validator."""
        from anuket.lib.validators import SecurePassword
        password = SecurePassword()
        # test than the validator is a formencode validators.String
        self.assertIsInstance(password, validators.String)
        # test than unsecure password are not accepted
        self.assertRaises(Invalid, password.validate_python, "PassW0rd", None)
        self.assertRaises(Invalid, password.validate_python, "123456789", None)
        self.assertRaises(Invalid, password.validate_python, "azerty", None)
        # tests than cracklib secure password are accepted
        secure_password = self.password_fixture()
        self.assertEqual(password.validate_python(secure_password, None),
                         secure_password)

    def test_UniqueAuthUsername(self):
        """ Test the ``UniqueAuthUsername`` validator."""
        self.dummy_user_fixture()
        from anuket.lib.validators import UniqueAuthUsername
        username = UniqueAuthUsername()
        # test than duplicate username is not accepted
        values = {'username': u'username'}
        self.assertRaises(Invalid, username.validate_python, values, None)
        # test than the validator do not raise an error in case of edition
        # of the user with the username
        values = {'user_id': 1, 'username': u'username'}
        self.assertEqual(username.validate_python(values, None), None)
        # test than empty username is allowed
        values = {'username': u''}
        self.assertEqual(username.validate_python(values, None), None)
        # test than empty values do not raise a KeyError
        values = {}
        self.assertEqual(username.validate_python(values, None), None)

    def test_UniqueAuthEmail(self):
        """ Test the ``UniqueAuthEmail`` validator."""
        self.dummy_user_fixture()
        from anuket.lib.validators import UniqueAuthEmail
        email = UniqueAuthEmail()
        # test than duplicate email is not accepted
        values = {'email': u'email@email.com'}
        self.assertRaises(Invalid, email.validate_python, values, None)
        # test than the validator do not raise an error in case of edition
        # of the user with the email
        values = {'user_id': 1, 'email': u'email@email.com'}
        self.assertEqual(email.validate_python(values, None), None)
        # test than empty email is allowed
        values = {'email': u''}
        self.assertEqual(email.validate_python(values, None), None)
        # test than empty values do not raise a KeyError
        values = {}
        self.assertEqual(email.validate_python(values, None), None)
