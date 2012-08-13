# -*- coding: utf-8 -*-
""" Authentification related utilities."""
from pyramid.security import unauthenticated_userid

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


def get_auth_user(request):
    """ Get the authenticated user id from the request and return an `AuthUser`
    object.

    :param request: a ``pyramid.request`` object
    """
    user_id = unauthenticated_userid(request)
    if user_id:
        return AuthUser.get_by_id(user_id)
