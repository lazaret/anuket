from pyramid.view import view_config


def includeme(config):
    """ Configure the Hello World routes."""
    config.add_route('hello', '/hello')
    config.add_route('hello_admin', '/hello/admin')


@view_config(route_name='hello', renderer='hello.mako')
def hello_world(request):
    """ Render the `Hello world` view."""
    hello = u"Hello World!"
    return dict(hello=hello)


@view_config(route_name='hello_admin', permission='admin',
             renderer='hello.mako')
def hello_admin(request):
    """ Render the `Hello admin` view."""
    hello = u"Hello Admin!"
    return dict(hello=hello)