# -*- coding: utf-8 -*-
from pyramid.security import Allow, Authenticated, ALL_PERMISSIONS


class RootFactory(object):
    """ Add ACLs to the default route factory."""
    __acl__ = [
        (Allow, Authenticated, 'view'),
        (Allow, 'group:admins', ALL_PERMISSIONS),
        ]

    def __init__(self, request):
        pass
