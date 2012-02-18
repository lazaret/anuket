<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>TITLE</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="img/favicon.ico">
    <link rel="stylesheet" href="static/css/bootstrap.min.css">
    <link rel="stylesheet" href="static/css/bootstrap-responsive.min.css">
    <link rel="stylesheet" href="static/css/style.css">

    <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
  </head>

  <body>
    <nav class="navbar navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <a class="brand" href="#">${brand_name}</a>
          <div class="nav-collapse">
            <ul class="nav">
              <li class="active"><a href="#"><span class="icon">S</span><b>Home</b></a></li>
              <!--<li class="active"><a href="#"><i class="icon-home icon-white"></i>&nbsp;<b>Home</b></a></li>-->
            </ul>
            <ul class="nav pull-right">
              <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown"><span class="icon">a</span><b>Tools</b><b class="caret"></b></a>
                <ul class="dropdown-menu">
                  <li><a href="#">Tool 1</a></li>
                  <li><a href="#">Tool 2</a></li>
                  <li><a href="#">Tool 3</a></li>
                  <li class="divider"></li>
                  <li><a href="#">Tool 4</a></li>
                </ul>
              </li>
              <li><a href="#"><span class="icon">t</span><b>Login</b></a></li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </nav>

    <div class="container">

      <h1>Bootstrap starter template</h1>
      <p>Use this document as a way to quick start any new project.<br> All you get is this message and a barebones HTML document.</p>

    </div> <!-- /container -->

    <!-- Le javascript - Placed at the end of the document so the pages load faster -->
    <script src="static/js/jquery.min.js"></script>
    <script src="static/js/bootstrap.min.js"></script>

    <script>$(function() {
      $('.dropdown-toggle').dropdown();}
      );
    </script>

  </body>
</html>
