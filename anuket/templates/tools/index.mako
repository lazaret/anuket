## -*- coding:utf-8 -*-
##
<%inherit file="anuket:templates/tools/base.mako" />


## Tools menu
<ul class="ca-menu">
  <li>
    <a href="${request.route_path('tools.user_list')}">
      <span class="ca-icon">L</span>
      <div class="ca-content">
        <h2 class="ca-main">${_(u"User management")}</h2>
      </div>
    </a>
  </li>
##  <li>
##    <a href="#">
##      <span class="ca-icon">F</span>
##      <div class="ca-content">
##        <h2 class="ca-main">Test</h2>
##      </div>
##    </a>
##  </li>
</ul>


## Page title
<%def name="page_title()">
${_(u"Tools")}
</%def>
