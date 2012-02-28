# -*- coding: utf-8 -*-
""" Admin tools for user management."""
from pyramid.view import view_config


def includeme(config):
    """Add user management routes."""
    config.add_route('tools.user_list', '/tools/user')
    config.add_route('tools.user_add', '/tools/user/add')
    config.add_route('tools.user_edit', '/tools/user/{id}/edit')
    config.add_route('tools.user_delete', '/tools/user/{id}/delete')
    config.add_route('tools.user_search', '/tools/user/search')

#TODO: add request_method ? (DELETE, POST, GET)
#TODO: put in a common class ? see http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/viewconfig.html#view-defaults-class-decorator

#@view_config(route_name='tools.user_list', renderer='wepwawet:templates/tools/user_list.mako', permission='admin')
@view_config(route_name='tools.user_list', renderer='wepwawet:templates/tools/user/user_list.mako')
def list(request):
    """Render the user list page."""
    return {'brand_name':'Wepwawet'}


@view_config(route_name='tools.user_add', renderer='wepwawet:templates/tools/user/user_add.mako')
def add(request):
    return {'brand_name':'Wepwawet'}


@view_config(route_name='tools.user_edit', renderer='wepwawet:templates/tools/user/user_edit.mako')
def edit(request):
    return {'brand_name':'Wepwawet'}


@view_config(route_name='tools.user_delete')
def delete(request):
    pass


@view_config(route_name='tools.user_search')
def search(request):
    pass