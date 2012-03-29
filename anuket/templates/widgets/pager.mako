## -*- coding:utf-8 -*-
##
<%def name="pager(page=None)">
    <% format='$link_previous ~3~ $link_next' %>
    <% link_attr={'class': 'btn btn-small'} %>
    <% curpage_attr={'class': 'btn btn-small btn-inverse disabled'} %>
    <% dotdot_attr={'class': 'btn btn-small disabled'} %>

    <div class="btn-group pull-right">
    ${page.pager(format=format,
                  link_attr=link_attr,
                  curpage_attr=curpage_attr,
                  dotdot_attr=dotdot_attr)}
    </div>
</%def>

