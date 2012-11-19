# -*- coding: utf-8 -*-
""" FormEncode validators."""
import logging
from formencode import Invalid
from formencode import validators

from anuket.lib.i18n import MessageFactory as _
from anuket.models.auth import AuthUser


log = logging.getLogger(__name__)


class FirstNameString(validators.String):
    """ Expand the validators.String class tu return a capitalised value
    with excessives inner whitespaces removed.
    """
    def _to_python(self, value, state):
        value = " ".join(value.split())
        return value.capitalize()


class LastNameString(validators.String):
    """ Expand the validators.String class tu return a value with excessives
    inner whitespaces removed.
    """
    # No capitalization here because is better to let the user to take care
    # of language exceptions like 'de Conty', 'de La Fontaine', 'Van de Walle'
    def _to_python(self, value, state):
        return " ".join(value.split())


class UsernamePlainText(validators.PlainText):
    """ Expand the validators.PlainText class tu return a lowercased value
    with all whitespaces removed.
    """
    def _to_python(self, value, state):
        return value.lower().replace(" ", "")


class UniqueAuthUsername(validators.FancyValidator):
    """ Unique username validator."""

    messages = {
        'not_unique_username': _(u"This username is already used")
    }

    def validate_python(self, values, state):
        """ Check for the uniqueness of `username`."""
        if 'username' in values:
            username = values['username']
            user = AuthUser.get_by_username(username)
        else:
            user = None  # no check for empty value
        # user_id is used to not raise an error when editing the user
        # the user_id must be available as hidden field in the edit form
        if 'user_id' in values:
            user_id = values['user_id']
        else:
            user_id = None
        if user and (user.user_id != user_id):
            errors = {'username': self.message('not_unique_username', state)}
            raise Invalid(self.message('not_unique_username', state),
                                       values, state, error_dict=errors)


class UniqueAuthEmail(validators.FancyValidator):
    """ Unique email validator."""

    messages = {
        'not_unique_email': _(u"This email is already used")
    }

    def validate_python(self, values, state):
        """ Check for the uniqueness of `email`."""
        if 'email' in values:
            email = values['email']
            user = AuthUser.get_by_email(email)
        else:
            user = None  # no check for None emails or empty value
        # user_id is used to not raise an error when editing the user
        # the user_id must be available as hidden field in the edit form
        if 'user_id' in values:
            user_id = values['user_id']
        else:
            user_id = None
        if user and (user.user_id != user_id):
            errors = {'email': self.message('not_unique_email', state)}
            raise Invalid(self.message('not_unique_email', state),
                                       values, state, error_dict=errors)

class NotOldPassword(validators.FancyValidator):
    """ Forbiden old password validator"""

    messages = {
        'old_password': _(u"Do not reuse your old password!")
    }

    def validate_python(self, values, state):
        """ Check tna the new password is not the same than the old one."""
        if 'password' in values:
            password = values['password']
        if 'user_id' in values:
            user_id = values['user_id']
            user = AuthUser.get_by_id(user_id)
        if user.check_password(user.username, password):
            errors = {'password': self.message('old_password', state)}
            raise Invalid(self.message('old_password', state),
                                       values, state, error_dict=errors)



class SecurePassword(validators.String):
    """ Secure password validator."""

    messages = {
        'not_secure': _(u"This password is not secure")
    }

    def validate_python(self, value, state):
        """ Use cracklib to check the strenght of passwords."""

        # try to import VeryFascistCheck from cracklib
        try:
            from cracklib import VeryFascistCheck
        except ImportError:
            log.warning('Cracklib module is missing!')
            return value

        # do the Very Fascist Check validation
        try:
            VeryFascistCheck(value)
        except ValueError:
            raise Invalid(self.message('not_secure', state), value, state)
        return value
