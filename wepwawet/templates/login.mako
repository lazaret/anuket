## -*- coding:utf-8 -*-
##
<%inherit file="wepwawet:templates/layout/base.mako" />

<div class="page-header">
  <h1>${_(u"Login")}</h1>
</div>

<div class="row">
  <div class="span5 offset2">
    <form action="/login" method="post" class="form-horizontal login-box">
      <fieldset>
        ${renderer.csrf_token()}
        <div class="control-group">
          <label for="username" class="control-label">${_(u"Username")}</label>
          <div class="controls">
            <input type="text" name="username" autofocus="autofocus" />
          </div>
        </div>
        <div class="control-group">
          <label for="password" class="control-label">${_(u"Password")}</label>
            <div class="controls">
              <input type="password" name="password" />
            </div>
        </div>
        <div class="form-actions">
          <button type="submit" name="form_submitted" class="btn btn-large btn-primary" >${_(u"Login")}</button>
        </div>
      </fieldset>
    </form>
  </div>
</div>
