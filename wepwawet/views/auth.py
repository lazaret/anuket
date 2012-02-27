# -*- coding: utf-8 -*-
from pyramid.httpexceptions import HTTPFound
from pyramid.security import forget, remember
from pyramid.view import view_config
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer
from wepwawet.forms import LoginForm
from wepwawet.security import USERS


def includeme(config):
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')


@view_config(route_name='login', renderer='wepwawet:templates/login.mako')
def login_view(request):
    """Render the login form."""
    form = Form(request, schema=LoginForm)
    if 'form_submitted' in request.params:
        username = request.params['username']
        password = request.params['password']
        if USERS.get(username) == password:
            headers = remember(request, username)
            request.session.flash(u"login ok", 'info') #TODO flash message
            return HTTPFound(location=request.route_path('home'), headers=headers)
        else:
            request.session.flash(u"login niet", 'error') #TODO flash message
    return dict(brand_name='Wepwawet',
                renderer=FormRenderer(form))

@view_config(route_name='logout')
def logout_view(request):
    """Clear credentials and retirect to the login page."""
    headers = forget(request)
    return HTTPFound(location=request.route_path('login'), headers=headers)