## -*- coding:utf-8 -*-
##
<%inherit file="wepwawet:templates/layout/base.mako" />

<div class="page-header">
  <h1>${_(u"User list")}</h1>
</div>

##<div class="page-header">
##<div>
##  <h1 class="pull-left">${_(u"User list")}</h1>
##  <div class="pull-right">
##    <a href='${request.route_path("tools.user_add")}' class='btn btn-primary'>${_(u"Add new user")}</a>
##
##<div class="form-search">
##<form class="form-search" method="get" action="${request.route_path('tools.user_list')}">
##  <input name="search" type="text" value="" placeholder="Search">
##</form>
##</div>
##
##    <form action="${request.route_path('tools.user_list')}" class="form-search">
##      <input type="text" name="search" placeholder="${_(u"Search")}" class="input-medium search-query">
##    </form>
##
##
##
##  </div>
##</div>
##</div>

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
  <tbody>
    <tr>
      <td>Test1</td>
      <td>Test2</td>
      <td>Test3</td>
      <td>Test4</td>
      <td>
        <div class="btn-group">
          <a href='${request.route_path("home")}' class='btn btn-mini'><span class="icon">z</span>${_(u"Show")}</a>
          <a href='${request.route_path("home")}' class='btn btn-mini'><span class="icon">></span>${_(u"Edit")}</a>
          <a href='${request.route_path("home")}' class='btn btn-mini'><span class="icon">Â</span>${_(u"Delete")}</a>
        </div>
      </td>
    </tr>
  </tbody>
</table>