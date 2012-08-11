# -*- coding: utf-8 -*-
""" Admin tools views for the application."""
import logging
from pyramid.view import view_config


log = logging.getLogger(__name__)


def includeme(config):
    """ Configure the tools home page route.

    :param config: a ``pyramid.config.Configurator`` object
    """
    config.add_route('tools.index', '/tools')


@view_config(route_name='tools.index', permission='admin',
             renderer='/tools/index.mako')
def tools_index_view(request):
    """ Render the tools home page.

    :param request: a ``pyramid.request`` object
    """
    return dict()
