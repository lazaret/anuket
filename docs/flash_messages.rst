Flash messages
--------------

To add flash messages from the views you can use the Pyramid flash messages
mecanisms. for example:

.. code-block:: python

request.session.flash(u"info message", 'info')
request.session.flash(u"success message", 'success')
request.session.flash(u"warning message", 'warn')
request.session.flash(u"error message", 'error')
