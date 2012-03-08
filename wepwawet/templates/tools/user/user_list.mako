## -*- coding:utf-8 -*-
##
<%inherit file="wepwawet:templates/layout/base.mako" />
<%namespace file="wepwawet:templates/layout/confirm_delete.mako" import="confirm_delete"/>
<%namespace file="wepwawet:templates/layout/pager.mako" import="pager"/>


<table class="table table-striped table-condensed">
  <thead>
    <tr>
      <th>${_(u"Username")}</th>
      <th>${_(u"First name")}</th>
      <th>${_(u"Last name")}</th>
      <th>${_(u"Email")}</th>
      <th style="width: 175px;"></th>
    </tr>
  </thead>
##  <tfoot>
##  </tfoot>
  <tbody>
    % for user in users:
    <tr>
      <td>${user.username}</td>
      <td>${user.first_name}</td>
      <td>${user.last_name}</td>
      <td>${user.email}</td>
      <td>
        <div class="btn-group">
          <a href="${request.route_path("home")}" class="btn btn-mini"><span class="icon">i</span>${_(u"Show")}</a>
          <a href="${request.route_path("tools.user_edit", user_id=user.user_id)}" class="btn btn-mini"><span class="icon">></span>${_(u"Edit")}</a>
          <a href="#confirm_delete" class="btn btn-mini" data-toggle="modal" onclick="$('#confirm_delete #delete_button').attr('href', '${request.route_path("tools.user_delete", user_id=user.user_id)}');"><span class="icon">Â</span>${_(u"Delete")}</a>
        </div>
      </td>
    </tr>
    % endfor
  </tbody>
</table>

## Pager
${pager(users)}

## Confirm delete modal
${confirm_delete()}


## Page title
<%def name="page_title()">
${_(u"User list")}
</%def>

## Add record button
<%def name="add_button()">
  <a href="${request.route_path("tools.user_add")}" class="btn btn-primary pull-right"><span class="icon">@</span>${_(u"Add new user")}</a>
</%def>

## Search box
<%def name="aside_search()">
<form action="${request.route_path('tools.user_list')}" class="well form-search">
  <input type="search" name="search" placeholder="${_(u"Search")}" class="input-small search-query">
<button type="submit" class="btn btn-small pull-right"><span class="icon">z</span>${_(u"Search")}</button>
</form>
</%def>
