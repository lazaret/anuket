## -*- coding:utf-8 -*-
##
<%inherit file="anuket:templates/tools/user/base.mako" />

<div class="row">
  <div class="span6 offset1">
    <div class="form-horizontal">
      <fieldset>
        <legend></legend>
        <div class="control-group">
          <label for="username" class="control-label">${_(u"Username")}</label>
          <div class="controls">
            <span class="input uneditable-input">${user.username}</span>
          </div>
        </div>
        <div class="control-group">
          <label for="username" class="control-label">${_(u"First name")}</label>
          <div class="controls">
            <span class="input uneditable-input">${user.first_name}</span>
          </div>
        </div>
        <div class="control-group">
          <label for="username" class="control-label">${_(u"Last name")}</label>
          <div class="controls">
            <span class="input uneditable-input">${user.last_name}</span>
          </div>
        </div>
        <div class="control-group">
          <label for="username" class="control-label">${_(u"Email")}</label>
          <div class="controls">
            <span class="input uneditable-input">${user.email}</span>
          </div>
        </div>
      </fieldset>
      <fieldset>
        <legend></legend>
        <div class="control-group">
          <label for="group_id" class="control-label">${_(u"Group")}</label>
          <div class="controls">
            <span class="input uneditable-input">${user.group.groupname}</span>
          </div>
        </div>
      </fieldset>
      <div class="form-actions">
        <div class="row">
          <div class="span2">
            <a href="${request.route_path("tools.user_edit", user_id=user.user_id)}" class="btn"><span class="icon">></span>${_(u"Edit")}</a>
          </div>
          <div class="span2">
            <a href="#confirm_delete" class="btn" data-toggle="modal" onclick="$('#confirm_delete #delete_button').attr('href', '${request.route_path("tools.user_delete", user_id=user.user_id)}');"><span class="icon">Ë</span>${_(u"Delete")}</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>


## Confirm delete modal
<%include file="anuket:templates/widgets/confirm_delete.mako"/>

## Page title
<%block name="page_title">
${_(u"User informations")}
</%block>
