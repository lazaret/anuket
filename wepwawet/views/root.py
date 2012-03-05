# -*- coding: utf-8 -*-
from pyramid.httpexceptions import HTTPFound
from pyramid.security import authenticated_userid
from pyramid.view import view_config, forbidden_view_config, notfound_view_config

#from ..models import (
#    DBSession,
#    MyModel,
#    )


def includeme(config):
    """Add root pages routes."""
    config.add_route('home', '/')


@notfound_view_config(renderer='wepwawet:templates/404.mako')
@view_config(route_name='home', renderer='wepwawet:templates/index.mako')
def root_view(request):
    """Render the root pages."""
#    request.session.flash(u"warning message", 'warn')
#    request.session.flash(u"info message", 'info')
#    request.session.flash(u"error message", 'error')
#    request.session.flash(u"success message", 'success')

    return dict(brand_name='Wepwawet')


@forbidden_view_config()
def forbiden_view(request):

    username = authenticated_userid(request)
    if username:
        request.session.flash(u"You do not have the permission to do this!", 'error')
        return HTTPFound(location=request.route_path('home'))
    else:
        request.session.flash(u"You are not connected, please log in.", 'error')
        return HTTPFound(location=request.route_path('login'))
