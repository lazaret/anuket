# -*- coding: utf-8 -*-
from formencode import compound
from formencode import validators
from formencode.schema import Schema


## helpers
def capitalize_string(value):
    """ Capitalize the first letter of the `value` string
    (and strip spaces).
    """
    return value.capitalize().strip()

def lower_string(value):
    """ Return the lowercase of `value` (and strip spaces)."""
    return value.lower().strip()

def strip_string(value):
    """ Revove leading and trailling spaces."""
    return value.strip()


class LoginForm(Schema):
    filter_extra_fields = True
    allow_extra_fields = True
    username = validators.String(not_empty=True)
    password = validators.String(not_empty=True)


class UserForm(Schema):
    """ Form validation schema for users."""
    filter_extra_fields = True
    allow_extra_fields = True

    username = compound.All(
        validators.String(min=5, max=16),
        validators.Wrapper(to_python=lower_string))
    first_name = compound.All(
        validators.String(not_empty=True),
        validators.Wrapper(to_python=capitalize_string))
    last_name = compound.All(
        validators.String(not_empty=True),
        validators.Wrapper(to_python=capitalize_string))
    email = validators.Email()
    password = compound.All(
        validators.String(min=6, max=80),
        validators.Wrapper(to_python=strip_string))
    password_confirm = validators.String()

    chained_validators = [
        validators.FieldsMatch('password', 'password_confirm'),
    ]




