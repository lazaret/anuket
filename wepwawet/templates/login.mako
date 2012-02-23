## -*- coding:utf-8 -*-
##
<%inherit file="wepwawet:templates/layout/base.mako" />

<div class="page-header">
  <h1>${_(u"Login")}</h1>
</div>

<div class="row">
  <div class="span5 offset2">
    <form class="form-horizontal login-box">
      <fieldset>
##        ${form.csrf_token()}
        <div class="control-group">
          <label for="input01" class="control-label">${_(u"Username")}</label>
          <div class="controls">
            <input type="text" autofocus="autofocus" id="input01" />
          </div>
        </div>
        <div class="control-group">
          <label for="input01" class="control-label">${_(u"Password")}</label>
            <div class="controls">
              <input type="password" id="input01" />
            </div>
        </div>
        <div class="form-actions">
          <button class="btn btn-large btn-primary" type="submit">${_(u"Login")}</button>
        </div>
      </fieldset>
    </form>
  </div>
</div>
