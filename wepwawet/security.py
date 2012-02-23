# -*- coding: utf-8 -*-


USERS = {'admin':'admin',
          'viewer':'viewer'}
GROUPS = {'admin':['group:admins']}

def groupfinder(userid, request):
    if userid in USERS:
        return GROUPS.get(userid, [])
