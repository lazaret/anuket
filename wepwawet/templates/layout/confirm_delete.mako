## -*- coding: utf-8 -*-
##
<%def name="confirm_delete()">
<div class="modal hide" id="confirm_delete">
  <div class="modal-header">
    <a class="close" data-dismiss="modal">×</a>
    <h3>${_("Confirm deletion")}</h3>
  </div>
  <div class="modal-body">
    <p><span class="icon">8</span>${_(u"Are you sure?")}</p>
  </div>
  <div class="modal-footer">
    <a href="#" class="btn" onclick="$('#confirm_delete').modal('hide')" >${_(u"Cancel")}</a>
##    <a href="${request.route_path("tools.user_delete", user_id=user.user_id)}" class="btn btn-danger">${_(u"Delete")}</a>

    </div>
</div>
</%def>

##TODO : add form + csrf_token + buttons + autococus on cancel
