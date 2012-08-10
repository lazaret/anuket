API Documentation
*****************


:mod:`anuket.models`
====================

.. automodule:: anuket.models

    .. autoclass:: AuthGroup

        .. automethod:: get_by_id

    .. autoclass:: AuthUser

        .. automethod:: get_by_id
        .. automethod:: get_by_username
        .. automethod:: get_by_email
        .. automethod:: check_password

    .. autoclass:: Migration

    .. autoclass:: RootFactory


:mod:`anuket.views`
===================

.. automodule:: anuket.views


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

.. autofunction:: anuket.views.user.user_add_view
.. autofunction:: anuket.views.user.user_delete_view
.. autofunction:: anuket.views.user.user_edit_view
.. autofunction:: anuket.views.user.user_list_view
.. autofunction:: anuket.views.user.user_show_view
.. autofunction:: anuket.views.user.password_edit_view


:mod:`anuket.scripts`
=====================

Database management
-------------------

.. automodule:: anuket.scripts

    .. autoclass:: InitializeDBCommand

        .. automethod:: run
        .. automethod:: initialize_db

    .. autoclass:: BackupDBCommand

        .. automethod:: run
        .. automethod:: backup_db

    .. autoclass:: UpgradeDBCommand

        .. automethod:: run
        .. automethod:: ubgrade_db


:mod:`anuket.lib`
=====================

Alembic utilities
-----------------

.. autofunction:: anuket.lib.alembic_utils.get_alembic_settings
.. autofunction:: anuket.lib.alembic_utils.get_alembic_revision


Translation
-----------

.. autofunction:: anuket.lib.i18n.locale_negotiator


Validators
----------

.. autoclass:: FirstNameString
.. autoclass:: LastNameString
.. autoclass:: UsernamePlainText
.. autoclass:: UniqueAuthUsername
.. autoclass:: UniqueAuthEmail
.. autoclass:: SecurePassword


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



