# -*- coding: utf-8 -*-
from formencode.schema import Schema
from formencode.validators import Email, FieldsMatch, Int, String

from wepwawet.lib.validators import CapitalString, UsernameString
from wepwawet.lib.validators import UniqueAuthEmail, UniqueAuthUsername


class LoginForm(Schema):
    filter_extra_fields = True
    allow_extra_fields = True


class UserForm(Schema):
    """ Form validation schema for users."""
    filter_extra_fields = True
    allow_extra_fields = True

    username = UsernameString(min=5, max=16, strip=True)
    first_name = CapitalString(not_empty=True, strip=True)
    last_name = CapitalString(not_empty=True, strip=True)
    email = Email()
    password = String(min=6, max=80, strip=True)
    password_confirm = String(min=6, max=80, strip=True)
    group_id = Int(not_empty=True)

    chained_validators = [
        FieldsMatch('password', 'password_confirm'),
        UniqueAuthUsername(),
        UniqueAuthEmail(),
    ]


class UserEditForm(UserForm):
    """ Form validation schema for user edit."""

    user_id = Int() #used in forms hidden field
    password = None
    password_confirm = None


class UserPasswordForm(UserForm):
    """ Form validation schema for user password change."""
    username = None
    first_name = None
    last_name = None
    email = None
    group_id = None

