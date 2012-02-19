from pyramid.view import view_config

#@view_config(route_name='home', renderer='anubis:templates/index.mako')
@view_config(route_name='home', renderer='index.mako')
def my_view(request):
    return {'brand_name':'Wepwawet'}
