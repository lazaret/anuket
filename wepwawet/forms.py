# -*- coding: utf-8 -*-
from formencode import validators
from formencode.schema import Schema


# TODO replace by a more complete user shema
# TODO move schemas in view files or models ?
class LoginForm(Schema):
    filter_extra_fields = True
    allow_extra_fields = True
    usename = validators.String(not_empty=True)
    password = validators.String(not_empty=True)
