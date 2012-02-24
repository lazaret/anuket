# -*- coding: utf-8 -*-
from pyramid.view import view_config

from ..models import (
    DBSession,
    MyModel,
    )


def includeme(config):
    """Add root pages routes."""
    config.add_route('home', '/')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
#    config.add_route('test', '/test')


@view_config(context='pyramid.exceptions.NotFound', renderer='wepwawet:templates/404.mako')
@view_config(route_name='home', renderer='wepwawet:templates/index.mako')
#@view_config(route_name='test', renderer='wepwawet:templates/index.mako', permission='test')
def root_view(request):
    """Render the root pages."""
#    request.session.flash(u"warning message", 'warn')
#    request.session.flash(u"info message", 'info')
#    request.session.flash(u"error message", 'error')
#    request.session.flash(u"success message", 'success')

    one = DBSession.query(MyModel).filter(MyModel.name=='one').first()
    return {'one':one, 'brand_name':'Wepwawet'}


#TODO redirect forbiden views + flash error
#@view_config(context='pyramid.exceptions.HTTPForbidden', renderer='wepwawet:templates/403.mako')


#---------------------------------------------------

from pyramid.httpexceptions import HTTPFound
from pyramid.security import forget, remember
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer
from wepwawet.forms import LoginForm
from wepwawet.security import USERS

@view_config(route_name='login', renderer='wepwawet:templates/login.mako')
def login_view(request):
    """Render the login form."""
    form = Form(request, schema=LoginForm)
    if 'form_submitted' in request.params:
        username = request.params['username']
        password = request.params['password']
        if USERS.get(username) == password:
            headers = remember(request, username)
            request.session.flash(u"login ok", 'info')
            return HTTPFound(location=request.route_path('home'), headers=headers)
        else:
            request.session.flash(u"login niet", 'error')
    return dict(brand_name='Wepwawet',
                renderer=FormRenderer(form))


@view_config(route_name='logout')
def logout_view(request):
    """Clear credentials and retirect to the login page."""
    headers = forget(request)
    return HTTPFound(location=request.route_path('login'), headers=headers)
