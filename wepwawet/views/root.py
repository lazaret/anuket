# -*- coding: utf-8 -*-
import logging
from pyramid.httpexceptions import HTTPFound
from pyramid.security import forget, remember
from pyramid.view import view_config, forbidden_view_config, notfound_view_config
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer

from wepwawet.lib.i18n import MessageFactory as _
from wepwawet.forms import LoginForm
from wepwawet.models import AuthUser


log = logging.getLogger(__name__)


def includeme(config):
    """Add root pages routes."""
    config.add_route('home', '/')
    config.add_route('about', '/about')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')


@notfound_view_config(renderer='404.mako')
@view_config(route_name='about', renderer='about.mako')
@view_config(route_name='home', renderer='index.mako')
def root_view(request):
    """Render the root pages."""
#    request.session.flash(u"warning message", 'warn')
#    request.session.flash(u"info message", 'info')
#    request.session.flash(u"error message", 'error')
#    request.session.flash(u"success message", 'success')
    return dict()


@forbidden_view_config()
def forbiden_view(request):
    """Redirect the 403 forbiden view to login or home page and add a
    flash message to display the relevant error.
    """
    #TODO: take care of csrf error
    if request.auth_user:
        request.session.flash(_(u"You do not have the permission to do this!"), 'error')
        return HTTPFound(location=request.route_path('home'))
    else:
        request.session.flash(_(u"You are not connected, please log in."), 'error')
        return HTTPFound(location=request.route_path('login'))


@view_config(route_name='login', renderer='login.mako')
def login_view(request):
    """Render the login form."""
    form = Form(request, schema=LoginForm)
    if 'form_submitted' in request.params and form.validate():
        username = request.params['username']
        password = request.params['password']
        if AuthUser.check_password(username, password):
            headers = remember(request, username)
            request.session.flash(_(u"You have successfuly connected."), 'info')
            return HTTPFound(location=request.route_path('home'), headers=headers)
        else:
            request.session.flash(_(u"Please check your login credentials!"), 'error')
    return dict(renderer=FormRenderer(form))


@view_config(route_name='logout')
def logout_view(request):
    """Clear credentials and redirect to the home page."""
    headers = forget(request)
    return HTTPFound(location=request.route_path('home'), headers=headers)
