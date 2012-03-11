# -*- coding: utf-8 -*-
from wepwawet.models import AuthUser, AuthGroup


def groupfinder(username, request):
    auth_user = AuthUser.get_by_username(username)
    if auth_user:
        auth_group = auth_user.group.groupname
        return [('group:%s' % auth_group)]
