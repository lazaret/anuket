# -*- coding: utf-8 -*-
from pyramid.view import view_config

from ..models import (
    DBSession,
#    MyModel,
    )


def includeme(config):
    """Add root pages routes."""
    config.add_route('home', '/')


@view_config(context='pyramid.exceptions.NotFound', renderer='wepwawet:templates/404.mako')
@view_config(route_name='home', renderer='wepwawet:templates/index.mako')
def root_view(request):
    """Render the root pages."""
#    request.session.flash(u"warning message", 'warn')
#    request.session.flash(u"info message", 'info')
#    request.session.flash(u"error message", 'error')
#    request.session.flash(u"success message", 'success')

#    one = DBSession.query(MyModel).filter(MyModel.name=='one').first()
#    return {'one':one, 'brand_name':'Wepwawet'}
    return {'brand_name':'Wepwawet'}



#@view_config(context='pyramid.exceptions.HTTPForbidden', renderer='wepwawet:templates/403.mako')
