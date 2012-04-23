## -*- coding:utf-8 -*-
##
<%! from pyramid.security import has_permission %>

<%def name="top_navbar()">
<nav role="navigation" class="navbar navbar-fixed-top">
  <div class="navbar-inner">
    <div class="container">
      <div class="nav-collapse">
        <ul class="nav">
          <li class="active"><a href="${request.route_path('home')}"><span class="icon">S</span><b>${_(u"Home")}</b></a></li>
        </ul>
        <ul class="nav pull-right">
        %if request.auth_user:
          ## Tools ara available only for admins
          % if has_permission('admin', request.context, request):
            <li><a href="${request.route_path('tools.index')}"><span class="icon">a</span><b>${_(u"Tools")}</b></a></li>
          %endif
          <li class="dropdown">
            <a href="#" data-toggle="dropdown" class="dropdown-toggle"><span class="icon">L</span><b>${request.auth_user.username}</b><b class="caret"/></b></a>
            <ul class="dropdown-menu">
              <li><a href="${request.route_path('logout')}">${_("Logout")}</a></li>
              <li><a href="#">Test</a></li>
            </ul>
          </li>
        %else:
          <li><a href="${request.route_path('login')}"><span class="icon">t</span><b>${_(u"Login")}</b></a></li>
        %endif
        </ul>
      </div><!--/.nav-collapse -->
    </div>
  </div>
</nav>
</%def>
