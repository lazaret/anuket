API Documentation
*****************

.. automodule:: anuket


:mod:`anuket.models` -- SQLAlchemy models
=========================================

.. automodule:: anuket.models

:mod:`anuket.models.auth` -- Auth model
---------------------------------------

.. automodule:: anuket.models.auth

    .. autoclass:: AuthGroup

        .. automethod:: get_by_id

    .. autoclass:: AuthUser

        .. automethod:: get_by_id
        .. automethod:: get_by_username
        .. automethod:: get_by_email
        .. automethod:: check_password

:mod:`anuket.models.migration` -- Migration model
-------------------------------------------------

.. automodule:: anuket.models.migration

    .. autoclass:: Migration

:mod:`anuket.models.rootfactory` -- RootFactory model
-----------------------------------------------------

.. automodule:: anuket.models.rootfactory

    .. autoclass:: RootFactory


:mod:`anuket.views` -- Pyramid views
====================================

.. automodule:: anuket.views


:mod:`anuket.views.root` -- Root views
--------------------------------------

.. automodule:: anuket.views.root

    .. autofunction:: root_view
    .. autofunction:: forbiden_view
    .. autofunction:: login_view
    .. autofunction:: logout_view


:mod:`anuket.views.tools` -- Tools views
----------------------------------------

.. automodule:: anuket.views.tools

    .. autofunction:: tools_index_view


:mod:`anuket.views.user` -- User views
--------------------------------------

.. automodule:: anuket.views.user

    .. autofunction:: user_add_view
    .. autofunction:: user_delete_view
    .. autofunction:: user_edit_view
    .. autofunction:: user_list_view
    .. autofunction:: user_show_view
    .. autofunction:: password_edit_view


:mod:`anuket.scripts` -- Console scripts
========================================

.. automodule:: anuket.scripts

:mod:`anuket.scripts.initializedb` -- Database initialization
-------------------------------------------------------------

.. automodule:: anuket.scripts.initializedb

    .. autoclass:: InitializeDBCommand

        .. automethod:: run
        .. automethod:: initialize_db

:mod:`anuket.scripts.backupdb` -- Database backup
-------------------------------------------------

.. automodule:: anuket.scripts.backupdb

    .. autoclass:: BackupDBCommand

        .. automethod:: run
        .. automethod:: backup_db

:mod:`anuket.scripts.upgradedb` -- Database upgrade
---------------------------------------------------

.. automodule:: anuket.scripts.upgradedb

    .. autoclass:: UpgradeDBCommand

        .. automethod:: run
        .. automethod:: upgrade_db


:mod:`anuket.lib` -- Internal libraries
=======================================

.. automodule:: anuket.lib

:mod:`anuket.lib.alembic_utils` -- Alembic utilities
----------------------------------------------------

.. automodule:: anuket.lib.alembic_utils

    .. autofunction:: get_alembic_settings
    .. autofunction:: get_alembic_revision


:mod:`anuket.lib.i18n` -- Translation library
---------------------------------------------

.. automodule:: anuket.lib.i18n

    .. autofunction:: locale_negotiator


:mod:`anuket.lib.validators` -- FormEncode Validators
-----------------------------------------------------

.. automodule:: anuket.lib.validators

    .. autoclass:: FirstNameString
    .. autoclass:: LastNameString
    .. autoclass:: UsernamePlainText
    .. autoclass:: UniqueAuthUsername

        .. automethod:: validate_python

    .. autoclass:: UniqueAuthEmail

        .. automethod:: validate_python

    .. autoclass:: SecurePassword

        .. automethod:: validate_python


Others
======

:mod:`anuket.security` -- Security
----------------------------------

.. automodule:: anuket.security

    .. autofunction:: groupfinder


:mod:`anuket.subscribers` -- Subscribers
----------------------------------------

.. automodule:: anuket.subscribers

    .. autofunction:: add_renderer_globals
    .. autofunction:: add_localizer
    .. autofunction:: add_csrf_validation
