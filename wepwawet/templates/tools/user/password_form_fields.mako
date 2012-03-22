## -*- coding:utf-8 -*-
##
<%def name="password_form_fields()">
<fieldset>
  <legend></legend>
  <div class="${'control-group error' if renderer.errors_for('password') else 'control-group'}">
    <label for="password" class="control-label">${_(u"Password")}</label>
    <div class="controls">
      <input type="password" name="password" autocomplete="off"/>
      % for message in renderer.errors_for('password'):
        <span class="help-inline"><span class="icon">8</span>${message}</span>
      % endfor
    </div>
  </div>
  <div class="${'control-group error' if renderer.errors_for('password_confirm') else 'control-group'}">
    <label for="password_confirm" class="control-label">${_(u"Confirm password")}</label>
    <div class="controls">
      <input type="password" name="password_confirm" autocomplete="off"/>
      % for message in renderer.errors_for('password_confirm'):
        <span class="help-inline"><span class="icon">8</span>${message}</span>
      % endfor
    </div>
  </div>
<fieldset>
</%def>
