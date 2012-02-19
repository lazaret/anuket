# -*- coding: utf-8 -*-
from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include(add_static_views)
    config.include(add_routes)
    config.scan()
    return config.make_wsgi_app()

def add_static_views(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

def add_routes(config):
    config.add_route('home', '/')
    config.add_route('login', '/login')
