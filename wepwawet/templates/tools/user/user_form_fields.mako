## -*- coding:utf-8 -*-
##
<%def name="user_form_fields()">
${renderer.csrf_token()}
<fieldset>
  <legend>${_(u"User informations")}</legend>
  <div class="${'control-group error' if renderer.errors_for('username') else 'control-group'}">
    <label for="username" class="control-label">${_(u"Username")}</label>
    <div class="controls">
      ${renderer.text("username", autofocus="autofocus")}
      % for message in renderer.errors_for('username'):
        <span class="help-inline"><span class="icon">8</span>${message}</span>
      % endfor
    </div>
  </div>
  <div class="${'control-group error' if renderer.errors_for('first_name') else 'control-group'}">
    <label for="first_name" class="control-label">${_(u"First name")}</label>
    <div class="controls">
      ${renderer.text("first_name")}
      % for message in renderer.errors_for('first_name'):
        <span class="help-inline"><span class="icon">8</span>${message}</span>
      % endfor
    </div>
  </div>
  <div class="${'control-group error' if renderer.errors_for('last_name') else 'control-group'}">
    <label for="last_name" class="control-label">${_(u"Last name")}</label>
    <div class="controls">
      ${renderer.text("last_name")}
      % for message in renderer.errors_for('last_name'):
        <span class="help-inline"><span class="icon">8</span>${message}</span>
      % endfor
    </div>
  </div>
  <div class="${'control-group error' if renderer.errors_for('email') else 'control-group'}">
    <label for="email" class="control-label">${_(u"Email")}</label>
    <div class="controls">
      ${renderer.text("email")}
      % for message in renderer.errors_for('email'):
        <span class="help-inline"><span class="icon">8</span>${message}</span>
      % endfor
    </div>
  </div>
</fieldset>
<fieldset>
  <legend></legend>
  <div class="${'control-group error' if renderer.errors_for('password') else 'control-group'}">
    <label for="password" class="control-label">${_(u"Password")}</label>
    <div class="controls">
      ${renderer.password("password")}
      % for message in renderer.errors_for('password'):
        <span class="help-inline"><span class="icon">8</span>${message}</span>
      % endfor
    </div>
  </div>
  <div class="${'control-group error' if renderer.errors_for('password_confirm') else 'control-group'}">
    <label for="password_confirm" class="control-label">${_(u"Confirm password")}</label>
    <div class="controls">
      <input type="password" name="password_confirm" />
      % for message in renderer.errors_for('password_confirm'):
        <span class="help-inline"><span class="icon">8</span>${message}</span>
      % endfor
    </div>
  </div>
<fieldset>
</%def>
