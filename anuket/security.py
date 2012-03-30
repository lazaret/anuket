# -*- coding: utf-8 -*-
from anuket.models import AuthUser


def groupfinder(username, request):
    """ Groupfinder callback for authentification policy.

    Return the groupname (principal) of an authenticated user form the
    database. Return None if the user do not exist."""
    auth_user = AuthUser.get_by_username(username)
    if auth_user:
        auth_group = auth_user.group.groupname
        return [('group:%s' % auth_group)]
