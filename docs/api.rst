API Documentation
*****************

Database schema
===============

.. automodule:: anuket.models

   .. autoclass:: AuthUser
      :members: get_by_id, get_by_username, check_password

   .. autoclass:: AuthGroup
      :members: get_by_id


Views
=====

Root views
----------

.. autofunction:: anuket.views.root.root_view
.. autofunction:: anuket.views.root.forbiden_view
.. autofunction:: anuket.views.root.login_view
.. autofunction:: anuket.views.root.logout_view


Tools view
----------

.. autofunction:: anuket.views.tools.tools_index_view


User views
----------

.. autofunction:: anuket.views.user.user_list_view
.. autofunction:: anuket.views.user.user_add_view
.. autofunction:: anuket.views.user.user_edit_view
.. autofunction:: anuket.views.user.user_delete_view


Others
======

Security
--------

.. autofunction:: anuket.security.groupfinder


Subscribers
-----------

.. autofunction:: anuket.lib.subscribers.add_renderer_globals
.. autofunction:: anuket.lib.subscribers.add_localizer
.. autofunction:: anuket.lib.subscribers.csrf_validation


Translation
-----------

.. autofunction:: anuket.lib.i18n.locale_negotiator


Database initialization
-----------------------

.. autofunction:: anuket.scripts.initializedb.initialize_db