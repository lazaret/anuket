API Documentation
*****************

Database schema
===============

.. automodule:: wepwawet.models

   .. autoclass:: AuthUser
      :members: get_by_id, get_by_username, check_password

   .. autoclass:: AuthGroup
      :members: get_by_id


Views
=====

Root views
----------

.. autofunction:: wepwawet.views.root.root_view
.. autofunction:: wepwawet.views.root.forbiden_view
.. autofunction:: wepwawet.views.root.login_view
.. autofunction:: wepwawet.views.root.logout_view


Tools view
----------

.. autofunction:: wepwawet.views.tools.tools_index_view


User views
----------

.. autofunction:: wepwawet.views.user.user_list_view
.. autofunction:: wepwawet.views.user.user_add_view
.. autofunction:: wepwawet.views.user.user_edit_view
.. autofunction:: wepwawet.views.user.user_delete_view


Others
======

Security
--------

.. autofunction:: wepwawet.security.groupfinder


Subscribers
-----------

.. autofunction:: wepwawet.lib.subscribers.add_renderer_globals
.. autofunction:: wepwawet.lib.subscribers.add_localizer
.. autofunction:: wepwawet.lib.subscribers.csrf_validation


Translation
-----------

.. autofunction:: wepwawet.lib.i18n.locale_negotiator


Database initialization
-----------------------

.. autofunction:: wepwawet.scripts.initializedb.initialize_db