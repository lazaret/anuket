# -*- coding: utf-8 -*-
""" Admin tools for user management."""
import logging
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer
from webhelpers import paginate

from wepwawet.lib.i18n import MessageFactory as _
from wepwawet.forms import UserForm
from wepwawet.models import DBSession, User


log = logging.getLogger(__name__)


def includeme(config):
    """Add user management routes."""
    config.add_route('tools.user_list', '/tools/user')
    config.add_route('tools.user_add', '/tools/user/add')
    config.add_route('tools.user_edit', '/tools/user/{user_id}/edit')
    config.add_route('tools.user_delete', '/tools/user/{user_id}/delete')
#    config.add_route('tools.user_search', '/tools/user/search')
#    config.add_route('tools.user_view', '/tools/user/{user_id}/view')


@view_config(route_name='tools.user_list', permission='admin', renderer='/tools/user/user_list.mako')
def list(request):
    """Render the user list page."""
    search = request.params.get('search')
    if search:
        users = DBSession.query(User).filter(User.username.like('%'+search+'%'))
    else:
        users = DBSession.query(User).all()
    page_url = paginate.PageURL_WebOb(request)
    users = paginate.Page(users,
                          page=int(request.params.get("page", 1)),
                          items_per_page=20,
                          url=page_url)
    return dict(users=users)


@view_config(route_name='tools.user_add', permission='admin', renderer='/tools/user/user_add.mako')
def add(request):
    form = Form(request, schema=UserForm)
    if 'form_submitted' in request.params and form.validate():
        user = form.bind(User())
        DBSession.add(user)
        request.session.flash(_(u"User added"), 'success')
        return HTTPFound(location=request.route_path('tools.user_list'))
    return dict(renderer=FormRenderer(form))


@view_config(route_name='tools.user_edit', permission='admin', renderer='/tools/user/user_edit.mako')
def edit(request):
    user_id = request.matchdict['user_id']
    user = DBSession.query(User).get(user_id)
    if not user:
        request.session.flash(_(u"This user did not exist!"), 'error')
        return HTTPFound(location=request.route_path('tools.user_list'))
    form = Form(request, schema=UserForm, obj=user)
    if 'form_submitted' in request.params and form.validate():
        form.bind(user)
        DBSession.add(user)
        request.session.flash(_(u"User updated"), 'success')
        return HTTPFound(location=request.route_path('tools.user_list'))
    return dict(renderer=FormRenderer(form))


@view_config(route_name='tools.user_delete', permission='admin')
def delete(request):
    user_id = request.matchdict['user_id']
    user = DBSession.query(User).get(user_id)
    if not user:
        request.session.flash(_(u"This user did not exist!"), 'error')
        return HTTPFound(location=request.route_path('tools.user_list'))
    DBSession.delete(user)
    request.session.flash(_(u"User deleted"), 'warning')
    return HTTPFound(location=request.route_path('tools.user_list'))


#@view_config(route_name='tools.user_search')
#def search(request):
#    pass

