## -*- coding:utf-8 -*-
##
<%namespace file="top_navbar.mako" import="top_navbar"/>
<%namespace file="flash_messages.mako" import="flash_messages"/>
<%namespace file="breadcrumbs.mako" import="breadcrumbs"/>

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>${self.page_title()}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="${request.static_url('wepwawet:static/img/favicon.ico')}">
    <link rel="stylesheet" href="${request.static_url('wepwawet:static/css/bootstrap.min.css')}">
    <link rel="stylesheet" href="${request.static_url('wepwawet:static/css/bootstrap-responsive.min.css')}">
    <link rel="stylesheet" href="${request.static_url('wepwawet:static/css/style.css')}">

    <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
##      <script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script>
      <script src="${request.static_url('wepwawet:static/js/html5shim.js')}"></script>
    <![endif]-->
  </head>

  <body>
    <header>
      ${top_navbar()}
    </header>

    <div class="container">
      <div class="row">
      <article role="main" class="span9">
        <div class ="flash-placeholder">
          ${flash_messages()}
        </div>
        ${next.body()}
      </article>
      <aside class="span3">
        <div class="well">
          <h1><img src="${request.static_url('wepwawet:static/img/wepwawet.svg')}" width=60>&nbsp;${brand_name}</h1>
        </div>
        <div style="padding: 8px 0pt;" class="well">
          <ul class="nav nav-list">
            <li class="nav-header">TESTING</li>
            <li class="active"><a href="#">Home</a></li>
            <li><a href="#">Test</a></li>
            <li><a href="#">Test</a></li>
            <li class="nav-header">Another TESTING</li>
            <li><a href="#">Test</a></li>
            <li><a href="#">Test</a></li>
            <li><a href="#">Test</a></li>
          </ul>
        </div>
      </aside>
      </div>
    </div><!-- /container -->
    <footer>
    </footer>

    <!-- javascrip imports -->
    <script src="${request.static_url('wepwawet:static/js/jquery.min.js')}"></script>
    <script src="${request.static_url('wepwawet:static/js/bootstrap.min.js')}"></script>

    <script>$(function() {
      $('.dropdown-toggle').dropdown();}
      );
    </script>

  </body>
</html>
##
<%def name="page_title()">TITLE</%def>
