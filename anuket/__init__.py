# -*- coding: utf-8 -*-
""" Anuket is an opiniated Python web framework based on Pyramid."""
from pyramid.config import Configurator
from pyramid.authentication import SessionAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid_beaker import session_factory_from_settings

from sqlalchemy import engine_from_config

from anuket import subscribers
from anuket.models import DBSession
from anuket.models.rootfactory import RootFactory
from anuket.security import groupfinder, get_auth_user
from anuket.views import root, tools, user


def add_authorization(config):
    """ Configure authorization and authentification.

    :param config: a ``pyramid.config.Configurator`` object
    """
    authorization_policy = ACLAuthorizationPolicy()
    authentication_policy = SessionAuthenticationPolicy(callback=groupfinder)
    config.set_authentication_policy(authentication_policy)
    config.set_authorization_policy(authorization_policy)


def add_static_views(config):
    """ Configure the static views.

    :param config: a ``pyramid.config.Configurator`` object
    """
    config.add_static_view('static', 'static', cache_max_age=3600)


def main(global_config, **settings):
    """ Configure and returns a Pyramid WSGI application.

    :param global_config: key/values from the [DEFAULT] section of an .ini fine
    :type global_config: dictionary
    :param **settings: key/values from the [app:main] section of an .ini fine
    :return: a ``pyramid.router.Router`` object
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
