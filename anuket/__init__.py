# -*- coding: utf-8 -*-
from pyramid.config import Configurator
from pyramid.security import unauthenticated_userid
from pyramid.authentication import SessionAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid_beaker import session_factory_from_settings

from sqlalchemy import engine_from_config

from anuket import subscribers
from anuket.models import DBSession, RootFactory, AuthUser
from anuket.security import groupfinder
from anuket.views import root, tools, user


def get_auth_user(request):
    """ Get the authenticated user id from the request and return an `AuthUser`
    object.
    """
    user_id = unauthenticated_userid(request)
    if user_id:
        return AuthUser.get_by_id(user_id)


def add_authorization(config):
    """ Configure authorization and authentification."""
    authorization_policy = ACLAuthorizationPolicy()
    authentication_policy = SessionAuthenticationPolicy(callback=groupfinder)
    config.set_authentication_policy(authentication_policy)
    config.set_authorization_policy(authorization_policy)


def add_static_views(config):
    """ Configure the static view."""
    config.add_static_view('static', 'static', cache_max_age=3600)


def main(global_config, **settings):
    """ Configure and returns a Pyramid WSGI application.
    """
    # configure SQLAlchemy
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    config = Configurator(settings=settings)
    # configure the root factory (used for Auth & Auth)
    root_factory = RootFactory
    config.set_root_factory(root_factory)
    # configure session
    session_factory = session_factory_from_settings(settings)
    config.set_session_factory(session_factory)
    # configure auth & auth
    config.include(add_authorization)
    # set an auth_user object
    config.set_request_property(get_auth_user, 'auth_user', reify=True)
    # configure subscribers
    config.include(subscribers)
    # configure static views
    config.include(add_static_views)
    # configure routes
    config.include(root)
    config.include(tools)
    config.include(user)
    # configure views
    config.scan()
    # configure i18n
    config.add_translation_dirs('anuket:locale')
    config.set_locale_negotiator('anuket.lib.i18n.locale_negotiator')
    return config.make_wsgi_app()
