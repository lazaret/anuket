# -*- coding: utf-8 -*-
from pyramid.view import view_config


#@view_config(route_name='home', renderer='wepwawet:templates/index.mako')
@view_config(route_name='home', renderer='index.mako')
def my_view(request):
    return {'brand_name':'Wepwawet'}

@view_config(route_name='login', renderer='login.mako')
def login_view(request):
    return {'brand_name':'Wepwawet'}
