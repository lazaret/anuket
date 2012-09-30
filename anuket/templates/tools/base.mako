## -*- coding:utf-8 -*-
##
<%inherit file="anuket:templates/base.mako" />

${next.body()}

## Aside tools menu
<%! active_menu = 'tool_list' %>
<%block name="aside_menu">
<div style="padding: 8px 0pt;" class="well">
  <ul class="nav nav-list">
    <li class="nav-header">${_(u"Tools")}</li>
    <li ${'class="active"' if self.attr.active_menu=='tool_list' else ''|n}>
      <a href="${request.route_path('tools.index')}"><span class="icon">a</span>${_(u"Tool list")}</a>
    </li>
    <li ${'class="active"' if self.attr.active_menu=='user_list' else ''|n}>
      <a href="${request.route_path('tools.user_list')}"><span class="icon">L</span>${_(u"User management")}</a>
    </li>
  </ul>
</div>
</%block>

## Nav bar active link
<%! active_link = 'tools' %>
