## -*- coding:utf-8 -*-
##
<%inherit file="anuket:templates/tools/user/base.mako" />
<%namespace file="anuket:templates/widgets/confirm_delete.mako" import="confirm_delete"/>
<%namespace file="anuket:templates/widgets/pager.mako" import="pager"/>


<table class="table table-striped table-condensed table-bordered">
  <thead>
    <tr>
      <th style="width: 50px;"></th>
      <th>${sortable_link('username', u"Username")}</th>
      <th>${sortable_link('first_name', u"First name")}</th>
      <th>${sortable_link('last_name', u"Last name")}</th>
      <th>${_(u"Email")}</th>
      <th>${_(u"Group")}</th>
    </tr>
  </thead>
##  <tfoot>
##  </tfoot>
  <tbody>
    % for user in users:
    <tr>
      <td> <!-- tool button -->
        <div class="btn-group">
          <button data-toggle="dropdown" class="btn btn-mini dropdown-toggle"><span class="icon">`</span> <span class="caret"/></button>
          <ul class="dropdown-menu">
            <li><a href="${request.route_path("tools.user_show", user_id=user.user_id)}"><span class="icon">z</span>${_(u"Show")}</a></li>
            <li><a href="${request.route_path("tools.user_edit", user_id=user.user_id)}"><span class="icon">></span>${_(u"Edit")}</a></li>
            <li><a href="${request.route_path("tools.password_edit", user_id=user.user_id)}"><span class="icon">t</span>${_(u"Change password")}</a></li>
            <li><a href="#confirm_delete" data-toggle="modal" onclick="$('#confirm_delete #delete_button').attr('href', '${request.route_path("tools.user_delete", user_id=user.user_id)}');"><span class="icon">Ë</span>${_(u"Delete")}</a></li>
          </ul>
        </div>
      </td>
      <td>${user.username}</td>
      <td>${user.first_name}</td>
      <td>${user.last_name}</td>
      <td>${user.email}</td>
      <td>${user.group.groupname}</td>
    </tr>
    % endfor
  </tbody>
</table>


## Pager
${pager(users)}

## Confirm delete modal
${confirm_delete()}



## Sortable column link
<%def name="sortable_link(column, textlink)">
  <% search = request.params.get('search') %>
  <% sort = request.params.get('sort') %>
  <% postlink = "?sort="+column %>
  %if search:
    <% postlink = postlink+"&search="+search %>
  %endif
  %if sort==column:
    <% arrow = u" ▾" %>
  %else:
    <% arrow = None %>
  %endif
  <a href="${request.route_path('tools.user_list')}${postlink}">${_(textlink)}${arrow}</a>
</%def>


## Page title
<%block name="page_title">
${_(u"User list")}
</%block>

## Add record button
<%block name="add_button">
<a href="${request.route_path("tools.user_add")}" class="btn btn-primary pull-right"><span class="icon">@</span>${_(u"Add new user")}</a>
</%block>

## Aside search box
<%block name="aside_search">
  <% search = request.params.get('search') %>
  %if search:
    <% placeholder = search %>
  %else:
    <% placeholder = _(u"Search") %>
  %endif
<form action="${request.route_path('tools.user_list')}" class="well form-search">
  <input type="search" name="search" placeholder="${placeholder}" class="input-small search-query">
<button type="submit" class="btn btn-small pull-right"><span class="icon">z</span>${_(u"Search")}</button>
</form>
</%block>

## Aside stats table
<%block name="aside_stats">
<table class="table table-condensed table-bordered">
  <thead>
   <tr><th>${_(u"Statistics")}</th></tr>
  <thead>
  <tbody>
    <tr>
      <td>${_("Users")}</td>
      <td>${stats['usercount']}</td>
    </tr>
    <tr>
      <td>${_("Groups")}</td>
      <td>${stats['groupcount']}</td>
    </tr>
  </tbody>
</table>
</%block>
