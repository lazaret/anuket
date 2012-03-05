# -*- coding: utf-8 -*-
""" Admin tools for the application."""
from pyramid.view import view_config


def includeme(config):
    """Add tools pages routes."""
    config.add_route('tools.index', '/tools')


@view_config(route_name='tools.index', renderer='wepwawet:templates/tools/tools_index.mako', permission='admin')
def tools_index_view(request):
    """Render the tools main page."""
    return {'brand_name':'Wepwawet'}
