## -*- coding:utf-8 -*-
##
<%inherit file="anuket:templates/tools/user/base.mako" />
<%namespace file="password_form_fields.mako" import="password_form_fields"/>


<div class="row">
  <div class="span7 offset1">
    <form action="" method="post" class="form-horizontal">
      ${renderer.csrf_token()}
      ${renderer.hidden('user_id')}
      ${password_form_fields()}
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
${_(u"Edit password")}
</%def>
