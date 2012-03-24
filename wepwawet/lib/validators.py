# -*- coding: utf-8 -*-
from formencode import Invalid
from formencode import validators

from wepwawet.models import AuthUser


class CapitalString(validators.String):
    """ Expand the validators.String class tu return a capitalised value."""
    def _to_python(self, value, state):
        return value.capitalize()


class UsernameString(validators.String):
    """ Expand the validators.String class tu return a lowercased value with
    all whitespaces removed."""
    def _to_python(self, value, state):
        return value.lower().replace(" ", "")


class UniqueAuthUsername(validators.FancyValidator):
    """ Unique username validator."""

    messages = {
        'not_unique_username': "This username is already used"
    }

    def validate_python(self, values, state):
        """ Check for the uniqueness of `username`."""
        username = values['username']
        user = AuthUser.get_by_username(username)
        # user_id is used to not raise an error when editing the user
        # the user_id must be available as hidden field in the edit form
        if values.has_key('user_id'):
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
        'not_unique_email': "This email is already used"
    }

    def validate_python(self, values, state):
        """ Check for the uniqueness of `email`."""
        email = values['email']
        if email: # no check for None emails
            user = AuthUser.get_by_email(email)
            # user_id is used to not raise an error when editing the user
            # the user_id must be available as hidden field in the edit form
            if values.has_key('user_id'):
                user_id = values['user_id']
            else:
                user_id = None
            if user and (user.user_id != user_id):
                errors = {'email': self.message('not_unique_email', state)}
                raise Invalid(self.message('not_unique_email', state),
                                           values, state, error_dict=errors)
