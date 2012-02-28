## -*- coding:utf-8 -*-
##
<%def name="user_form_fields()">
<fieldset>
  <legend>${_(u"User informations")}</legend>
  <div class="control-group">
    <label for="username" class="control-label">${_(u"Username")}</label>
    <div class="controls">
      <input type="text" name="username" autofocus="autofocus" />
    </div>
  </div>
  <div class="control-group">
    <label for="first_name" class="control-label">${_(u"First name")}</label>
    <div class="controls">
      <input type="text" name="first_name" />
    </div>
  </div>
  <div class="control-group">
    <label for="last_name" class="control-label">${_(u"Last name")}</label>
    <div class="controls">
      <input type="text" name="last_name" />
    </div>
  </div>
  <div class="control-group">
    <label for="email" class="control-label">${_(u"Email")}</label>
    <div class="controls">
      <input type="text" name="email" />
    </div>
  </div>
</fieldset>
<fieldset>
  <legend></legend>
  <div class="control-group">
    <label for="password" class="control-label">${_(u"Password")}</label>
    <div class="controls">
      <input type="password" name="password" />
    </div>
  </div>
  <div class="control-group">
    <label for="confirm_password" class="control-label">${_(u"Confirm password")}</label>
    <div class="controls">
      <input type="password" name="confirm_password" />
    </div>
  </div>
<fieldset>
</%def>
