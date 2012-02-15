from pyramid.view import view_config

@view_config(route_name='home', renderer='anubis:templates/mytemplate.pt')
def my_view(request):
    return {'project':'Anubis'}
