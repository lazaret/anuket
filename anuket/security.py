# -*- coding: utf-8 -*-
""" Authentification related utilities."""
from anuket.models.auth import AuthUser


def groupfinder(user_id, request):
    """ Groupfinder callback for authentification policy.

    Return the groupname (principal) of an authenticated user form the
    database. Return None if the user do not exist.

    :param user_id: the id of the authenticated user
    :type user_id: integer
    :param request: a ``pyramid.request`` object
    :return: the user groupname or None
    """
    auth_user = AuthUser.get_by_id(user_id)
    if auth_user:
        auth_group = auth_user.group.groupname
        return [('group:%s' % auth_group)]


#TODO move get_auth_user here ?
