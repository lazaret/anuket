## -*- coding:utf-8 -*-
##
<%def name="top_navbar()">
<nav role="navigation" class="navbar navbar-fixed-top">
  <div class="navbar-inner">
    <div class="container">
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
          <li><a href="login"><span class="icon">t</span><b>Login</b></a></li>
        </ul>
      </div><!--/.nav-collapse -->
    </div>
  </div>
</nav>
</%def>
