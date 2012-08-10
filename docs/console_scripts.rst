Console scripts
***************

Anuket provide console scripts:

* ``initialize_anuket_db``
* ``backup_anuket_db``
* ``upgrade_anuket_db``


Initializing the database
=========================

``initialize_anuket_db`` is a script used to initialize your SQLAlchemy
database.

.. code-block:: text

    $ initialize_anuket_db development.ini

The script will create a database by using the ``sqlalchemy.url`` option
from the .ini file, and will fill it with default values.


Backup the database
===================

``backup_anuket_db`` is a script used to backup your database.

.. code-block:: text

    $ backup_anuket_db development.ini

The script will create a bziped SQL dump of your database using the
``anuket.backup_directory`` option from the .ini file
(/var/backups by default). The filename will include the date of the backup.


Upgrade the database
====================

``upgrade_anuket_db`` is a script used to upgrade your database in case of
database schema change in future Anuket versions. The database schemas changes
are maitained by using Alembic_.

.. code-block:: text

    $ upgrade_anuket_db development.ini

The script will check first if there is an up-to-date database backup, and if
it's the case, it will perform the upgrade of the database by using Alembic.

If you prefer, you can also use Alembic directly to maintain your database.
For example :

.. code-block:: text

    $ alembic -c development.ini -n app:main upgrade head

This will directly perform the database upgrade, but without checking for a
database backup.


.. _Alembic: http://pypi.python.org/pypi/alembic
