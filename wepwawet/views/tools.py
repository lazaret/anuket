# -*- coding: utf-8 -*-
""" Admin tools for the application."""
import logging
from pyramid.security import authenticated_userid
from pyramid.view import view_config


log = logging.getLogger(__name__)


def includeme(config):
    """Add tools pages routes."""
    config.add_route('tools.index', '/tools')


@view_config(route_name='tools.index', permission='admin', renderer='/tools/tools_index.mako')
def tools_index_view(request):
    """Render the tools main page."""
    return dict(username=authenticated_userid(request))