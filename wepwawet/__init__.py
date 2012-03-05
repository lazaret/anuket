# -*- coding: utf-8 -*-
from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from sqlalchemy import engine_from_config

from .lib import subscribers
from .models import DBSession, RootFactory
from .security import groupfinder
from .views import auth, root, tools, user


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    # configure SQLAlchemy
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    config = Configurator(settings=settings)
    # configure the root factory (used for Auth & Auth)
    root_factory = RootFactory
    config.set_root_factory(root_factory)
    # configure session
    session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
    config.set_session_factory(session_factory)

    # configure auth & auth
    authorization_policy = ACLAuthorizationPolicy()
    #TODO use SessionAuthenticationPolicy ?
    authentication_policy = AuthTktAuthenticationPolicy('sosecret', callback=groupfinder)
    config.set_authentication_policy(authentication_policy)
    config.set_authorization_policy(authorization_policy)

    # configure subscribers
    config.include(subscribers)
    # configure static views
    config.include(add_static_views)
    # configure routes
    config.include(auth)
    config.include(root)
    config.include(tools)
    config.include(user)
    # configure views
    config.scan()
    # configure i18n
    config.add_translation_dirs('wepwawet:locale')
    config.set_locale_negotiator('wepwawet.lib.i18n.locale_negotiator')
    return config.make_wsgi_app()


def add_static_views(config):
    """ Congigure the static view."""
    config.add_static_view('static', 'static', cache_max_age=3600)

