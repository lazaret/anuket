## -*- coding:utf-8 -*-
##
<%inherit file="anuket:templates/tools/user/base.mako" />
<%namespace file="user_form_fields.mako" import="user_form_fields"/>
<%namespace file="password_form_fields.mako" import="password_form_fields"/>


<div class="row">
  <div class="span7 offset1">
    <form action="" method="post" class="form-horizontal">
      ${renderer.csrf_token()}

      <fieldset>
        <legend></legend>
        <div class="control-group">
          <label for="username" class="control-label">${_(u"Username")}</label>
          <div class="controls">
            ${renderer.text('username', autofocus='autofocus')}
          </div>
        </div>
        <div class="control-group">
          <label for="first_name" class="control-label">${_(u"First name")}</label>
          <div class="controls">
            ${renderer.text('first_name')}

            <span class="help-inline radio-toggle">
              <span class="btn-group">
                <label for="first_name_or" class="btn btn-mini btn-success active toggle-or">${_("OR")}</label>
                <label for="first_name_and" class="btn btn-mini toggle-and">${_("AND")}</label>
              </span>
              <input type="radio" id="first_name_or" name="first_name_or" checked />
              <input type="radio" id="first_name_and" name="first_name_and" />
            </span>

          </div>
        </div>
        <div class="control-group">
          <label for="last_name" class="control-label">${_(u"Last name")}</label>
          <div class="controls">
            ${renderer.text('last_name')}

            <span class="help-inline radio-toggle">
              <span class="btn-group">
                <label for="last_name_or" class="btn btn-mini btn-success active toggle-or">${_("OR")}</label>
                <label for="last_name_and" class="btn btn-mini toggle-and">${_("AND")}</label>
              </span>
              <input type="radio" id="last_name_or" name="last_name_or" checked />
              <input type="radio" id="last_name_and" name="last_name_and" />
            </span>

          </div>
        </div>
      </fieldset>
      <div class="form-actions">
        <div class="row">
          <div class="span2">
            <button type="submit" name="form_submitted" class="btn btn-primary"><span class="icon">Ã</span>${_(u"Search")}</button>
          </div>
        </div>
      </div>
    </form>
  </div>
</div>






## Page title
<%def name="page_title()">
${_(u"Advanced user search")}
</%def>




