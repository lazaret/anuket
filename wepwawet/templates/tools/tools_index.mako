## -*- coding:utf-8 -*-
##
<%inherit file="wepwawet:templates/layout/base.mako" />

%if username:
    ${username}
%endif


## Page title
<%def name="page_title()">
${_(u"Tools")}
</%def>

