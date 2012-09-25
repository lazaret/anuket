## -*- coding:utf-8 -*-
##
<%inherit file="anuket:templates/base.mako" />

<div class="row">
  <div class="span5 offset2">
    <form action="/login" method="post" class="form-horizontal login-box">
      ${renderer.csrf_token()}
      <fieldset>
        <div class="control-group">
          <label for="username" class="control-label">${_(u"Username")}</label>
          <div class="controls">
            <input type="username" name="username" autofocus="autofocus"/>
          </div>
        </div>
        <div class="control-group">
          <label for="password" class="control-label">${_(u"Password")}</label>
            <div class="controls">
            <input type="password" name="password"/>
            </div>
        </div>
        <div class="form-actions">
          <button type="submit" name="form_submitted" class="btn btn-large btn-primary" >${_(u"Login")}</button>
        </div>
      </fieldset>
    </form>
  </div>
</div>

## Page title
<%block name="page_title">
${_(u"Login")}
</%block>
