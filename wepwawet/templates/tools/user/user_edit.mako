## -*- coding:utf-8 -*-
##
<%inherit file="wepwawet:templates/tools/base.mako" />
<%namespace file="user_form_fields.mako" import="user_form_fields"/>


<div class="row">
  <div class="span7 offset1">
    <form action="" method="post" class="form-horizontal">
      ${user_form_fields()}
      <div class="form-actions">
        <div class="row">
          <div class="span2">
            <button type="submit" name="form_submitted" class="btn btn-primary"><span class="icon">Ã</span>${_(u"Update")}</button>
          </div>
          <div class="span2">
            <button type="button" onclick="window.location='/tools/user'" class="btn"><span class="icon">Â</span>${_(u"Cancel")}</button>
          </div>
        </div>
      </div>
    </form>
  </div>
</div>

## Page title
<%def name="page_title()">
${_(u"Edit user")}
</%def>
