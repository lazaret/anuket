# -*- coding: utf-8 -*-
from pyramid.config import Configurator
from .views import root

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include(add_static_views)
    # include routes
    config.include(root)
    config.scan()
    return config.make_wsgi_app()

def add_static_views(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
