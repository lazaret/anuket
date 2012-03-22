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
from wepwawet.models import DBSession, AuthUser, AuthGroup


log = logging.getLogger(__name__)


def includeme(config):
    """Add user management routes."""
    config.add_route('tools.user_list', '/tools/user')
    config.add_route('tools.user_add', '/tools/user/add')
    config.add_route('tools.user_show', '/tools/user/{user_id}/show')
    config.add_route('tools.user_edit', '/tools/user/{user_id}/edit')
    config.add_route('tools.user_delete', '/tools/user/{user_id}/delete')
#    config.add_route('tools.user_search', '/tools/user/search')


def get_grouplist():
    groups = DBSession.query(AuthGroup).order_by(AuthGroup.groupname).all()
    grouplist = [(group.group_id, group.groupname) for group in groups]
    return grouplist


@view_config(route_name='tools.user_list', permission='admin', renderer='/tools/user/user_list.mako')
def user_list_view(request):
    """ Render the user list page."""
    sortable_columns = ['username', 'first_name', 'last_name']
    column = request.params.get('sort')
    search = request.params.get('search')
    # construct the query
    users = DBSession.query(AuthUser)
    if column and column in sortable_columns:
        users = users.order_by(column)
    else:
        users = users.order_by(AuthUser.username)
    if search:
        users = users.filter(AuthUser.username.like('%'+search+'%'))


    #TODO add a flash message for empty searchs

    page_url = paginate.PageURL_WebOb(request)
    users = paginate.Page(users,
                          page=int(request.params.get("page", 1)),
                          items_per_page=20,
                          url=page_url)
    return dict(users=users)


@view_config(route_name='tools.user_add', permission='admin', renderer='/tools/user/user_add.mako')
def user_add_view(request):
    """ Render the add user form."""
    grouplist = get_grouplist()
    form = Form(request, schema=UserForm)
    if 'form_submitted' in request.params and form.validate():
        user = form.bind(AuthUser())
        DBSession.add(user)
        request.session.flash(_(u"User added successfully."), 'success')
        return HTTPFound(location=request.route_path('tools.user_list'))
    return dict(renderer=FormRenderer(form),
                grouplist=grouplist)


@view_config(route_name='tools.user_show', permission='admin', renderer='/tools/user/user_show.mako')
def user_show_view(request):
    """ Render the show user datas page."""
    user_id = request.matchdict['user_id']
    user = AuthUser.get_by_id(user_id)
    if not user:
        request.session.flash(_(u"This user did not exist!"), 'error')
        return HTTPFound(location=request.route_path('tools.user_list'))
    return dict(user=user)


@view_config(route_name='tools.user_edit', permission='admin', renderer='/tools/user/user_edit.mako')
def user_edit_view(request):
    """ Render the edit user form."""
    user_id = request.matchdict['user_id']
    user = AuthUser.get_by_id(user_id)
    if not user:
        request.session.flash(_(u"This user did not exist!"), 'error')
        return HTTPFound(location=request.route_path('tools.user_list'))
    grouplist = get_grouplist()
    form = Form(request, schema=UserForm, obj=user)
    if 'form_submitted' in request.params and form.validate():
        form.bind(user)
        DBSession.add(user)
        request.session.flash(_(u"User updated successfully."), 'success')
        return HTTPFound(location=request.route_path('tools.user_list'))
    return dict(renderer=FormRenderer(form),
                grouplist=grouplist)
    #TODO move password fields to password_edit_view


@view_config(route_name='tools.user_delete', permission='admin')
def user_delete_view(request):
    """ Delete an user."""
    user_id = request.matchdict['user_id']
    user = AuthUser.get_by_id(user_id)
    if not user:
        request.session.flash(_(u"This user did not exist!"), 'error')
        return HTTPFound(location=request.route_path('tools.user_list'))
    DBSession.delete(user)
    request.session.flash(_(u"User deleted."), 'warning')
    return HTTPFound(location=request.route_path('tools.user_list'))


#@view_config(route_name='tools.password_edit', permission='admin', renderer='/tools/user/password_edit.mako')
#def password_edit_view(request):
#    """ Render the change password form."""
#    pass


#@view_config(route_name='tools.user_search', permission='admin', renderer='/tools/user/user_search.mako')
#def user_search_view(request):
#    pass
