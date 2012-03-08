# -*- coding: utf-8 -*-
from formencode import validators


class CapitalString(validators.String):
    """Expand the validators.String class tu return a capitalised value."""
    def _to_python(self, value, state):
        return value.capitalize()


class UsernameString(validators.String):
    """Expand the validators.String class tu return a lowercased value with
    all whitespaces removed."""
    def _to_python(self, value, state):
        return value.lower().replace(" ","")


