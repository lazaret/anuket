# -*- coding: utf-8 -*-
""" Main views for the application."""
import logging
from formencode.schema import Schema
from pyramid.httpexceptions import HTTPFound
from pyramid.security import forget, remember
from pyramid.view import view_config, forbidden_view_config
from pyramid.view import notfound_view_config
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer

from anuket.models.auth import AuthUser


log = logging.getLogger(__name__)


def includeme(config):
    """ Configure the root pages routes.

    Configure the home, about, login and logout pages routes.

    :param config: a ``pyramid.config.Configurator`` object
    """
    config.add_route('home', '/')
    config.add_route('about', '/about')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')


@notfound_view_config(renderer='404.mako')
@view_config(route_name='about', renderer='about.mako')
@view_config(route_name='home', renderer='index.mako')
def root_view(request):
    """ Render the root pages.

    Render the home page, the login page and 404 not found page.

    :param request: a ``pyramid.request`` object
    """
    _ = request.translate
    #check the default admin password if any admin is connected
    from pyramid.security import has_permission
    if has_permission('admin', request.context, request):
        if AuthUser.check_password(username=u'admin', password=u'admin'):
            request.session.flash(_("Change the default password!"),
                                  'error')
    return dict()


@forbidden_view_config()
def forbiden_view(request):
    """ Redirect the 403 forbiden view.

    Authenticated user with not enought permission are redirected to the home
    page. Non-autenthicaded users are redirected to the login page.
    A corresponding flash message is also added to the error message queue.

    :param request: a ``pyramid.request`` object
    """
    _ = request.translate
    if request.auth_user:
        request.session.flash(_(u"Insufficient permissions!"),
                              'error')
        return HTTPFound(location=request.route_path('home'))
    else:
        request.session.flash(_(u"You are not connected."),
                              'error')
        return HTTPFound(location=request.route_path('login'))


@view_config(route_name='login', renderer='login.mako')
def login_view(request):
    """ Render the login form.

    Display an empty login form or check the submited credentials with the ones
    from the database. Add a success flash message, an userid in the cookies
    and redirect to the home page if the credentials are goods. Add an error
    flash message and display again the login form if the credentials are
    wrong.

    :param request: a ``pyramid.request`` object
    """
    _ = request.translate
    form = Form(request, schema=LoginForm)
    if 'form_submitted' in request.params and form.validate():
        username = request.params['username']
        password = request.params['password']
        if AuthUser.check_password(username, password):
            auth_user = AuthUser.get_by_username(username)
            headers = remember(request, auth_user.user_id)
            request.session.flash(_(u"Successful login."),
                                  'success')
            return HTTPFound(location=request.route_path('home'),
                             headers=headers)
        else:
            request.session.flash(_(u"Check your login credentials!"),
                                  'error')
    return dict(renderer=FormRenderer(form))


@view_config(route_name='logout')
def logout_view(request):
    """ Logout authenticated user.

    Clear the credentials of the connected user if any. Then, redirect to the
    home page and add a info flash message.

    :param request: a ``pyramid.request`` object
    """
    _ = request.translate
    headers = forget(request)
    request.session.flash(_(u"You have been disconnected."), 'info')
    return HTTPFound(location=request.route_path('home'), headers=headers)


# Formencode schema
class LoginForm(Schema):
    """ Form validation schema for login."""
    filter_extra_fields = True
    allow_extra_fields = True
