## -*- coding:utf-8 -*-
##
<%! from pyramid.security import has_permission %>

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title><%block name="page_title"/></title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="${request.static_url('anuket:static/img/favicon.ico')}">
    <link rel="stylesheet" href="${request.static_url('anuket:static/css/bootstrap.min.css')}">
    <link rel="stylesheet" href="${request.static_url('anuket:static/css/bootstrap-responsive.min.css')}">
    <link rel="stylesheet" href="${request.static_url('anuket:static/css/style.css')}">

    <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
##      <script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script>
      <script src="${request.static_url('anuket:static/js/html5shim.js')}"></script>
    <![endif]-->
  </head>

  <body>

## Top navigation bar
    ## default active navigation link
    <%! active_link = 'home' %>
    <nav role="navigation" class="navbar navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <div class="nav-collapse">
            ## left navbar
            <ul class="nav">
              <li ${'class="active"' if self.attr.active_link=='home' else ''|n}>
                <a href="${request.route_path('home')}"><span class="icon">S</span><b>${_(u"Home")}</b></a>
              </li>
              <%block name="left_navbar_links">
              </%block>
            </ul>
            ## right navbar
            <ul class="nav pull-right">
            %if request.auth_user:
              ## Tools are available only for admins
              % if has_permission('admin', request.context, request):
                <li ${'class="active"' if self.attr.active_link=='tools' else ''|n}>
                  <a href="${request.route_path('tools.index')}"><span class="icon">a</span><b>${_(u"Tools")}</b></a>
                </li>
              %endif
                <li class="dropdown">
                  <a href="#" data-toggle="dropdown" class="dropdown-toggle"><span class="icon">L</span><b>${request.auth_user.username}</b><b class="caret"/></b></a>
                  <ul class="dropdown-menu">
                    <li><a href="${request.route_path('logout')}">${_("Logout")}</a></li>
                  </ul>
                </li>
            %else:
              <li ${'class="active"' if self.attr.active_link=='login' else ''|n}>
                <a href="${request.route_path('login')}"><span class="icon">t</span><b>${_(u"Login")}</b></a>
              </li>
            %endif
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </nav>

## Main header
    <header>
      <div class="container">
        <div class="row">
          <div class="span9">
            <div class ="flash-placeholder">
              <%include file="anuket:templates/widgets/flash_messages.mako"/>
            </div>
            <div class="row">
              <div class="span6">
                <h1>${self.page_title()}</h1>
              </div>
              <div class="span3">
                <%block name="add_button"/>
              </div>
            </div>
          </div>
          <div class="span3">
            <%block name="aside_logo">
            <div class="well">
              <h1><img src="${request.static_url('anuket:static/img/anuket.svg')}" width=60>&nbsp;${brand_name}</h1>
            <div>
            </%block>
          </div>
        </div>
      </div>
    </header>

## Main body and aside blocks
    <div class="container">
      <div class="row">
      <article role="main" class="span9">
        ${next.body()}
      </article>
      <aside class="span3">
        <%block name="aside_menu"/>
        <%block name="aside_search"/>
        <%block name="aside_stats"/>
      </aside>
      </div>
    </div><!-- /container -->

## Main footer
    <footer>
      <%block name="footer"/>
    </footer>

## Javascript imports
    <script src="${request.static_url('anuket:static/js/jquery.min.js')}"></script>
    <script src="${request.static_url('anuket:static/js/bootstrap.min.js')}"></script>
    <script src="${request.static_url('anuket:static/js/anuket.js')}"></script>

  </body>
</html>
