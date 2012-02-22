# -*- coding: utf-8 -*-
from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig
#from pyramid.authentication import AuthTktAuthenticationPolicy
#from pyramid.authorization import ACLAuthorizationPolicy
from .views import root, tools
from .lib import subscribers


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    # configure session
    session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
    config.set_session_factory(session_factory)
#    # configure auth & auth
#    authorization_policy = ACLAuthorizationPolicy()
#    authentication_policy = AuthTktAuthenticationPolicy('seekrit') #TODO use SessionAuthenticationPolicy ?
#    config.set_authentication_policy(authentication_policy)
#    config.set_authorization_policy(authorization_policy)

    # configure subscribers
    config.include(subscribers)
    # configure static views
    config.include(add_static_views)
    # configure routes
    config.include(root)
    config.include(tools)
    # configure views
    config.scan()
    # configure i18n
    config.add_translation_dirs('wepwawet:locale')
    config.set_locale_negotiator('wepwawet.lib.i18n.locale_negotiator')
    return config.make_wsgi_app()


def add_static_views(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

#TODO: Auth & auth
#TODO: decide if we use beaker for sessions
