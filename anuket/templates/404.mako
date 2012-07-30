## -*- coding:utf-8 -*-
##
<%inherit file="anuket:templates/base.mako" />


<h3>${_(u"The page you requested was not found.")}</h3>


## Page title
<%def name="page_title()">
404 - ${_(u"Page not found!")}
</%def>
