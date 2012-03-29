# -*- coding: utf-8 -*-
import logging
from pyramid.httpexceptions import HTTPFound
from pyramid.security import forget, remember
from pyramid.view import view_config, forbidden_view_config
from pyramid.view import notfound_view_config
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer

from anuket.lib.i18n import MessageFactory as _
from anuket.forms import LoginForm
from anuket.models import AuthUser


log = logging.getLogger(__name__)


def includeme(config):
    """Configure the root pages routes.

    Configure the home, about, login and logout pages routes.
    """
    config.add_route('home', '/')
    config.add_route('about', '/about')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')


@notfound_view_config(renderer='404.mako')
@view_config(route_name='about', renderer='about.mako')
@view_config(route_name='home', renderer='index.mako')
def root_view(request):
    """Render the root pages.

    Render the home page, the login page and 404 not found page.

    Return:
        An empty dict.
    """
    return dict()


@forbidden_view_config()
def forbiden_view(request):
    """Redirect the 403 forbiden view.

    Authenticated user with not enought permission are redirected to the home
    page. Non-autenthicaded users are redirected to the login page. A
    corresponding flash message is also added to the error message queue.

    Args:
        request: Pyramid Request object representing the current WSGI request.

    Returns:
        location: the home or login route path.
    """
    if request.auth_user:
        request.session.flash(_(u"You do not have the permission to do this!"),
                              'error')
        return HTTPFound(location=request.route_path('home'))
    else:
        request.session.flash(_(u"You are not connected, please log in."),
                              'error')
        return HTTPFound(location=request.route_path('login'))


@view_config(route_name='login', renderer='login.mako')
def login_view(request):
    """Render the login form.

    Display an empty login form or check the submited credentials with the ones
    from the database. Redirect to the home page if the credentials are goods.
    Add an error flash message if they are wrong and display again the login
    form.

    Args:
        request: Pyramid Request object representing the current WSGI request.

    Returns:
        headers: add the authenticated userid to the request.
        location: the home or login route path.
        renderer: pyramid_simpleform.Form object.
    """
    form = Form(request, schema=LoginForm)
    if 'form_submitted' in request.params and form.validate():
        username = request.params['username']
        password = request.params['password']
        if AuthUser.check_password(username, password):
            headers = remember(request, username)
            request.session.flash(_(u"You have successfuly connected."),
                                  'info')
            return HTTPFound(location=request.route_path('home'),
                             headers=headers)
        else:
            request.session.flash(_(u"Please check your login credentials!"),
                                  'error')
    return dict(renderer=FormRenderer(form))


@view_config(route_name='logout')
def logout_view(request):
    """Logout authenticated user.

    Clear the credentials of the connected user if any. Then, redirect to the
    home page and add a informational flash message.

    Args:
        request: Pyramid Request object representing the current WSGI request.

    Returns:
        headers: clear the userid from the request.
        location: the home route path.
    """
    headers = forget(request)
    request.session.flash(_(u"You have been disconnected."), 'info')
    return HTTPFound(location=request.route_path('home'), headers=headers)
