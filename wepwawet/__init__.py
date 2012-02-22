# -*- coding: utf-8 -*-
from pyramid.config import Configurator
#from pyramid.authentication import AuthTktAuthenticationPolicy
#from pyramid.authorization import ACLAuthorizationPolicy
from .views import root, tools

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
#    authorization_policy = ACLAuthorizationPolicy()
#    authentication_policy = AuthTktAuthenticationPolicy('seekrit') #TODO use SessionAuthenticationPolicy ?
#    # TODO see https://bitbucket.org/cancel/pyrone/src/087372020b67/pyrone/__init__.py
    config = Configurator(settings=settings)
#    # set auth & auth
#    config.set_authentication_policy(authentication_policy)
#    config.set_authorization_policy(authorization_policy)
    config.include(add_static_views)
    # include routes
    config.include(root)
    config.include(tools)
    # scan views
    config.scan()
    # incluse suscribers
    config.add_subscriber('wepwawet.subscribers.add_renderer_globals', 'pyramid.events.BeforeRender')
    config.add_subscriber('wepwawet.subscribers.add_localizer', 'pyramid.events.NewRequest')
    #
    config.add_translation_dirs('wepwawet:locale')
    return config.make_wsgi_app()

def add_static_views(config):
    config.add_static_view('static', 'static', cache_max_age=3600)


#def add_suscribers(config):
#    config.add_subscriber('wepwawet.subscribers.add_renderer_globals', 'pyramid.events.BeforeRender')
#    config.add_subscriber('wepwawet.subscribers.add_localizer', 'pyramid.events.NewRequest')