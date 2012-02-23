# -*- coding: utf-8 -*-
from pyramid.view import view_config


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
    return {'brand_name':'Wepwawet'}


#TODO redirect forbiden views + flash error
#@view_config(context='pyramid.exceptions.HTTPForbidden', renderer='wepwawet:templates/403.mako')


from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer
from wepwawet.forms import LoginForm

@view_config(route_name='login', renderer='wepwawet:templates/login.mako')
def login_view(request):
    """Render the login form."""
    form = Form(request, schema=LoginForm)
    return {'brand_name':'Wepwawet', 'form':FormRenderer(form)}


from pyramid.httpexceptions import HTTPFound
from pyramid.security import forget

@view_config(route_name='logout')
def logout_view(request):
    """Clear credentials and retirect to the home page."""
    headers = forget(request)
    return HTTPFound(location=request.route_path('home'), headers=headers)