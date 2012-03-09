## -*- coding: utf-8 -*-
##
<%def name="confirm_delete()">
  <div id="confirm_delete" class="modal hide"">
    <div class="modal-header">
      <a class="close" data-dismiss="modal">×</a>
      <h3>${_("Confirm deletion")}</h3>
    </div>
    <div class="modal-body">
      <h4>${_("Are you sure?")}</h4>
      <p>${_("Do you really want to delete this user?")}</p>
    </div>
    <div class="modal-footer">
      <a href="" id="delete_button" class="btn btn-danger">${_(u"Delete")}</a>
      <a href="" class="btn" data-dismiss="modal">${_("Cancel")}</a>
    </div>
  </div>
</%def>