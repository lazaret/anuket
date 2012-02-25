# -*- coding: utf-8 -*-
from pyramid.security import Allow, Everyone


class RootFactory(object):
    __acl__ = [ (Allow, Everyone, 'view'),
                (Allow, 'group:admins', 'admin') ]
    def __init__(self, request):
        pass
