## -*- coding:utf-8 -*-
##
<%inherit file="wepwawet:templates/layout/base.mako" />
<%namespace file="user_form_fields.mako" import="user_form_fields"/>

<div class="page-header">
  <h1>${_(u"Add user")}</h1>
</div>

<div class="row">
  <div class="span5 offset2">
    <form action="" method="post" class="form-horizontal">
      ${user_form_fields()}
      <div class="form-actions">
        <div class="row">
          <div class="span1">
            <button type="submit" name="form_submitted" class="btn btn-primary" >${_(u"Submit")}</button>
          </div>
          <div class="span1">
            <button type="button" onclick="window.location='/tools/user'" class="btn">${_(u"Cancel")}</button>
          </div>
        </div>
      </div>
    </form>
  </div>
</div>