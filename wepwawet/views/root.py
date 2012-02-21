# -*- coding: utf-8 -*-
from pyramid.view import view_config


def includeme(config):
    """Add root pages routes."""
    config.add_route('home', '/')
    config.add_route('login', '/login')
    config.add_route('test', '/test')

@view_config(context='pyramid.exceptions.NotFound', renderer='wepwawet:templates/404.mako')
@view_config(route_name='home', renderer='wepwawet:templates/index.mako')
@view_config(route_name='login', renderer='wepwawet:templates/login.mako')
#@view_config(route_name='test', renderer='wepwawet:templates/index.mako', permission='test')
def root_view(request):
    """Render the root pages."""
    return {'brand_name':'Wepwawet'}

# for forbiden views
#@view_config(context='pyramid.exceptions.HTTPForbidden', renderer='wepwawet:templates/403.mako')
