## -*- coding:utf-8 -*-
##
<%namespace file="wepwawet:templates/widgets/top_navbar.mako" import="top_navbar"/>
<%namespace file="wepwawet:templates/widgets/flash_messages.mako" import="flash_messages"/>

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
    ${top_navbar()}
    <header>
      <div class="container">
        <div class="row">
          <div class="span9">
            <div class ="flash-placeholder">
              ${flash_messages()}
            </div>
            <div class="row">
              <div class="span6">
                <h1>${self.page_title()}</h1>
              </div>
              <div class="span3">
                ${self.add_button()}
              </div>
            </div>
          </div>
          <div class="span3">
            <div class="well">
              <h1><img src="${request.static_url('wepwawet:static/img/wepwawet.svg')}" width=60>&nbsp;${brand_name}</h1>
            <div>
          </div>
        </div>
      </div>
    </header>

    <div class="container">
      <div class="row">
      <article role="main" class="span9">
        ${next.body()}
      </article>
      <aside class="span3">
        ${self.aside_menu()}
        ${self.aside_search()}
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

## Page title
<%def name="page_title()"></%def>

## Add record button
<%def name="add_button()"></%def>

## Aside menu
<%def name="aside_menu()"></%def>

## Aside search box
<%def name="aside_search()"></%def>
