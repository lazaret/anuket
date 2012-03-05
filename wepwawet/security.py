# -*- coding: utf-8 -*-


USERS = {'admin':'admin', # user:pass
          'viewer':'viewer'}
GROUPS = {'admin':['group:admins']} # user:group

def groupfinder(userid, request):
    if userid in USERS:
        return GROUPS.get(userid, [])
