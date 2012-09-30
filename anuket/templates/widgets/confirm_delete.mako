## -*- coding: utf-8 -*-
##
<%block name="confirm_delete">
<div id="confirm_delete" class="modal hide"">
  <div class="modal-header">
    <a class="close" data-dismiss="modal">×</a>
    <h3>${_("Confirm deletion")}</h3>
  </div>
  <div class="modal-body">
    <div class="row">
      <div class="span1">
        <span class="icon" style="color: #da4f49; font-size: 4em;">8</span>
      </div>
      <div class="span4">
        <h4>${_("Are you sure?")}</h4>
        <p>${_("Do you really want to delete this user?")}</p>
      </div>
    </div>
  </div>
  <div class="modal-footer">
    <a href="" id="delete_button" class="btn btn-danger"><span class="icon">Ë</span>${_(u"Delete")}</a>
    <a href="" class="btn" data-dismiss="modal"><span class="icon">Â</span>${_("Cancel")}</a>
  </div>
</div>
</%block>
