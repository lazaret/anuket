## -*- coding:utf-8 -*-
##
<%inherit file="wepwawet:templates/layout/base.mako" />

##<div class="page-header">
##  <h1>${_(u"User list")}</h1>
##</div>

##<div class="page-header">
##<div>
##  <h1 class="pull-left">${_(u"User list")}</h1>
##  <div class="pull-right">
##    <a href="${request.route_path("tools.user_add")}" class="btn btn-primary">${_(u"Add new user")}</a>
##


##  </div>
##</div>
##</div>

##<table class="table table-striped table-condensed">
<table class="table table-striped">
  <thead>
    <tr>
      <th>${_(u"Username")}</th>
      <th>${_(u"First name")}</th>
      <th>${_(u"Last name")}</th>
      <th>${_(u"Email")}</th>
      <th style="width: 175px;"></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Test1</td>
      <td>Test2</td>
      <td>Test3</td>
      <td>Test4</td>
      <td>
        <div class="btn-group">
          <a href='${request.route_path("home")}' class='btn btn-mini'><span class="icon">i</span>${_(u"Show")}</a>
          <a href='${request.route_path("home")}' class='btn btn-mini'><span class="icon">></span>${_(u"Edit")}</a>
          <a href='${request.route_path("home")}' class='btn btn-mini'><span class="icon">Â</span>${_(u"Delete")}</a>
        </div>
      </td>
    </tr>
  </tbody>
</table>

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
