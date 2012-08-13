# -*- coding: utf-8 -*-
""" Admin tools for user management."""
import logging
from formencode.schema import Schema
from formencode.validators import Email, FieldsMatch, Int, String
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer
from webhelpers import paginate

from anuket.lib.validators import FirstNameString, LastNameString
from anuket.lib.validators import SecurePassword, UniqueAuthUsername
from anuket.lib.validators import UniqueAuthEmail, UsernamePlainText
from anuket.models import DBSession
from anuket.models.auth import AuthUser, AuthGroup


log = logging.getLogger(__name__)


def includeme(config):
    """ Configure the user management pages routes.

    Configure the list, add, show, edit, delete and change password pages
    routes.

    :param config: a ``pyramid.config.Configurator`` object
    """
    config.add_route('tools.user_list', '/tools/user')
    config.add_route('tools.user_add', '/tools/user/add')
    config.add_route('tools.user_show', '/tools/user/{user_id}/show')
    config.add_route('tools.user_edit', '/tools/user/{user_id}/edit')
    config.add_route('tools.user_delete', '/tools/user/{user_id}/delete')
#    config.add_route('tools.user_search', '/tools/user/search')
    config.add_route('tools.password_edit', '/tools/user/{user_id}/password')


def get_grouplist():
    """ Generate a list of groups from the database.

    :return: a list of pair values (`group_id`, `groupname`)
    :rtype: list
    """
    # For use in group select forms.
    groups = DBSession.query(AuthGroup).order_by(AuthGroup.groupname).all()
    grouplist = [(group.group_id, group.groupname) for group in groups]
    return grouplist


def get_user_stats():
    """ Get basic database statistics.

    :return: users and groups counts from the database
    :rtype: dictionary
    """
    usercount = DBSession.query(AuthUser.user_id).count()
    groupcount = DBSession.query(AuthGroup.group_id).count()
    return dict(usercount=usercount, groupcount=groupcount)


@view_config(route_name='tools.user_list', permission='admin',
             renderer='/tools/user/user_list.mako')
def user_list_view(request):
    """ Render the user list page.

    Return a paged user list from the database. The paged list can be
    ordered by username, first name or last name. Add an error flash message
    if the list is empty. Return also basic users statistics.

    :param request: a ``pyramid.request`` object
    """
    _ = request.translate
    stats = get_user_stats()
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
        users = users.filter(AuthUser.username.like('%' + search + '%'))
    # add a flash message for empty results
    if users.count() == 0:
        request.session.flash(_(u"There is no results!"), 'error')
    # paginate results
    page_url = paginate.PageURL_WebOb(request)
    users = paginate.Page(users,
                          page=int(request.params.get("page", 1)),
                          items_per_page=20,
                          url=page_url)
    return dict(users=users, stats=stats)


@view_config(route_name='tools.user_add', permission='admin',
             renderer='/tools/user/user_add.mako')
def user_add_view(request):
    """ Render the add user form page.

    Display an empty user form or validate the user submited form. If the form
    is validated then add the user datas to the database and a success flash
    message. If the form is not valid, then display again the form with
    validation errors. Return also a list of groups to use in the group select
    form.

    :param request: a ``pyramid.request`` object
    """
    _ = request.translate
    grouplist = get_grouplist()
    form = Form(request, schema=UserForm)
    if 'form_submitted' in request.params and form.validate():
        user = form.bind(AuthUser())
        DBSession.add(user)
        request.session.flash(_(u"User added."), 'success')
        return HTTPFound(location=request.route_path('tools.user_list'))
    return dict(renderer=FormRenderer(form),
                grouplist=grouplist)


@view_config(route_name='tools.user_show', permission='admin',
             renderer='/tools/user/user_show.mako')
def user_show_view(request):
    """ Render the show user datas page.

    Seek the database for the user datas based on user_id used in the route. If
    the user did not exist then add an error flash message and redirect to the
    user list. If the user exist then return his datas.

    :param request: a ``pyramid.request`` object
    """
    _ = request.translate
    user_id = request.matchdict['user_id']
    user = AuthUser.get_by_id(user_id)
    if not user:
        request.session.flash(_(u"This user did not exist!"), 'error')
        return HTTPFound(location=request.route_path('tools.user_list'))
    return dict(user=user)


@view_config(route_name='tools.user_edit', permission='admin',
             renderer='/tools/user/user_edit.mako')
def user_edit_view(request):
    """ Render the edit user form page.

    Seek the database for the user datas based on user_id used in the route. If
    the user did not exist then add an error flash message and redirect to the
    user list.
    If the user exist then render the user form filled with the user datas. If
    the form is validated then change the user datas to the database and add
    success flash message. If the form is not valid, then display again the
    form with validation errors. Return also a list of groups to use in the
    group select form.

    :param request: a ``pyramid.request`` object
    """
    _ = request.translate
    user_id = request.matchdict['user_id']
    user = AuthUser.get_by_id(user_id)
    if not user:
        request.session.flash(_(u"This user did not exist!"), 'error')
        return HTTPFound(location=request.route_path('tools.user_list'))
    grouplist = get_grouplist()
    form = Form(request, schema=UserEditForm, obj=user)
    if 'form_submitted' in request.params and form.validate():
        form.bind(user)
        DBSession.add(user)
        request.session.flash(_(u"User updated."), 'success')
        return HTTPFound(location=request.route_path('tools.user_list'))
    return dict(renderer=FormRenderer(form),
                grouplist=grouplist)


@view_config(route_name='tools.user_delete', permission='admin')
def user_delete_view(request):
    """ Delete an user.

    Seek the database for the user datas based on user_id used in the route. If
    the user did not exist then add an error flash message and redirect to the
    user list. If the user exist then delete the user in the database, add a
    warning flash message and then redirect to the user list.

    :param request: a ``pyramid.request`` object
    """
    # The confirm delete must be managed by modal messages in the templates,
    # and we forbid direct deletion from the address bar (no referer)
    _ = request.translate
    if not request.referer:
        request.session.flash(_(u"Insufficient permissions!"),
                              'error')
        return HTTPFound(location=request.route_path('home'))

    user_id = request.matchdict['user_id']
    user = AuthUser.get_by_id(user_id)
    if not user:
        request.session.flash(_(u"This user did not exist!"), 'error')
        return HTTPFound(location=request.route_path('tools.user_list'))

    #forbid the deletion if it's the only admin user
    if user.group.groupname == u'admins':
        adminscount = DBSession.query(AuthUser.user_id).join(AuthGroup).\
                                filter(AuthGroup.groupname == u'admins').\
                                count()
        if adminscount == 1:
            request.session.flash(_(u"Deletion of the only admin forbidden!"),
                                  'error')
            return HTTPFound(location=request.route_path('tools.user_list'))

    DBSession.delete(user)
    request.session.flash(_(u"User deleted."), 'warn')
    return HTTPFound(location=request.route_path('tools.user_list'))


@view_config(route_name='tools.password_edit', permission='admin',
             renderer='/tools/user/password_edit.mako')
def password_edit_view(request):
    """ Render the change password form page.

    Seek the database for the user datas based on user_id used in the route. If
    the user did not exist then add an error flash message and redirect to the
    user list.
    If the user exist then render an empty password form. If the form is
    validated then change the user password in the database and add
    success flash message. If the form is not valid, then display again the
    form with validation errors.

    :param request: a ``pyramid.request`` object
    """
    _ = request.translate
    user_id = request.matchdict['user_id']
    user = AuthUser.get_by_id(user_id)
    if not user:
        request.session.flash(_(u"This user did not exist!"), 'error')
        return HTTPFound(location=request.route_path('tools.user_list'))
    form = Form(request, schema=UserPasswordForm, obj=user)
    if 'form_submitted' in request.params and form.validate():
        form.bind(user)
        DBSession.add(user)
        request.session.flash(_(u"Password updated."), 'success')
        return HTTPFound(location=request.route_path('tools.user_list'))
    return dict(renderer=FormRenderer(form))


#@view_config(route_name='tools.user_search', permission='admin',
#              renderer='/tools/user/user_search.mako')
#def user_search_view(request):
#    grouplist = get_grouplist()
#    form = Form(request, schema=UserForm)
#    return dict(renderer=FormRenderer(form),
#                grouplist=grouplist)


# FormEncode schemas
class UserForm(Schema):
    """ Form validation schema for users."""
    filter_extra_fields = True
    allow_extra_fields = True

    username = UsernamePlainText(min=5, max=16, strip=True)
    first_name = FirstNameString(not_empty=True, strip=True)
    last_name = LastNameString(not_empty=True, strip=True)
    email = Email()
    password = SecurePassword(min=6, max=80, strip=True)
    password_confirm = String(strip=True)
    group_id = Int(not_empty=True)

    chained_validators = [
        FieldsMatch('password', 'password_confirm'),
        UniqueAuthUsername(),
        UniqueAuthEmail(),
    ]


class UserEditForm(UserForm):
    """ Form validation schema for user edit."""
    user_id = Int()  # used in forms hidden field
    password = None
    password_confirm = None


class UserPasswordForm(UserForm):
    """ Form validation schema for user password change."""
    user_id = Int()  # used in forms hidden field
    username = None
    first_name = None
    last_name = None
    email = None
    group_id = None

    chained_validators = [
        FieldsMatch('password', 'password_confirm'),
    ]
