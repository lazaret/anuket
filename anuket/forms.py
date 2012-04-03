# -*- coding: utf-8 -*-
from formencode.schema import Schema
from formencode.validators import Email, FieldsMatch, Int, String

from anuket.lib.validators import FirstNameString
from anuket.lib.validators import LastNameString
from anuket.lib.validators import UsernamePlainText
from anuket.lib.validators import UniqueAuthEmail
from anuket.lib.validators import UniqueAuthUsername
from anuket.lib.validators import SecurePassword


class LoginForm(Schema):
    """ Form validation schema for login."""
    filter_extra_fields = True
    allow_extra_fields = True


class UserForm(Schema):
    """ Form validation schema for users."""
    filter_extra_fields = True
    allow_extra_fields = True

    username = UsernamePlainText(min=5, max=16, strip=True)
    first_name = FirstNameString(not_empty=True, strip=True)
    last_name = LastNameString(not_empty=True, strip=True)
    email = Email()
    password = SecurePassword(min=6, max=80, strip=True)
    password_confirm = String(strip=True)
    group_id = Int(not_empty=True)

    chained_validators = [
        FieldsMatch('password', 'password_confirm'),
        UniqueAuthUsername(),
        UniqueAuthEmail(),
    ]


class UserEditForm(UserForm):
    """ Form validation schema for user edit."""
    user_id = Int()  # used in forms hidden field
    password = None
    password_confirm = None


class UserPasswordForm(UserForm):
    """ Form validation schema for user password change."""
    user_id = Int()  # used in forms hidden field
    username = None
    first_name = None
    last_name = None
    email = None
    group_id = None

    chained_validators = [
        FieldsMatch('password', 'password_confirm'),
    ]
