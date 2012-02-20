# -*- coding: utf-8 -*-
from pyramid.view import view_config

def includeme(config):
    """Add root pages routes."""
    config.add_route('home', '/')
    config.add_route('login', '/login')

#@view_config(route_name='home', renderer='wepwawet:templates/index.mako')
@view_config(context='pyramid.exceptions.NotFound', renderer='404.mako')
@view_config(route_name='home', renderer='index.mako')
@view_config(route_name='login', renderer='login.mako')
def root_view(request):
    """Render the root pages."""
    return {'brand_name':'Wepwawet'}
