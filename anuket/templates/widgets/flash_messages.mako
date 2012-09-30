## -*- coding:utf-8 -*-
##

<%block name="flash_messages">
    % for queue in ['info', 'warn', 'error', 'success']:
        % for message in request.session.pop_flash(queue):
            <div class="alert alert-${queue}">
              <a class="close" data-dismiss="alert">×</a>
              ${message}
            </div>
        % endfor
    % endfor
## messages with no queue are info messages
    % for message in request.session.pop_flash():
        <div class="alert alert-info">
            <a class="close" data-dismiss="alert">×</a>
            ${message}
        </div>
    % endfor
</%block>

