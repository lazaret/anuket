## -*- coding:utf-8 -*-
##
<%def name="top_navbar()">
<nav role="navigation" class="navbar navbar-fixed-top">
  <div class="navbar-inner">
    <div class="container">
      <div class="nav-collapse">
        <ul class="nav">
          <li class="active"><a href="${request.route_path('home')}"><span class="icon">S</span><b>${_(u"Home")}</b></a></li>
        </ul>
        <ul class="nav pull-right">
          <li class="dropdown">
            <a href="${request.route_path('tools.index')}" class="dropdown-toggle" data-toggle="dropdown"><span class="icon">a</span><b>${_(u"Tools")}</b><b class="caret"></b></a>
            <ul class="dropdown-menu">
                <li><a href="#">Tool 1</a></li>
                <li><a href="#">Tool 2</a></li>
                <li><a href="#">Tool 3</a></li>
                <li class="divider"></li>
                <li><a href="#">Tool 4</a></li>
            </ul>
          </li>
          <li><a href="${request.route_path('login')}"><span class="icon">t</span><b>${_(u"Login")}</b></a></li>
        </ul>
      </div><!--/.nav-collapse -->
    </div>
  </div>
</nav>
</%def>
