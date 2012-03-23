# -*- coding: utf-8 -*-
from pyramid.security import Allow, Authenticated, Everyone, ALL_PERMISSIONS


class RootFactory(object):
    __acl__ = [
#        (Allow, Everyone, 'view'),
        (Allow, Authenticated, 'view'),
        (Allow, 'group:admins', ALL_PERMISSIONS),
        ]

    def __init__(self, request):
        pass
