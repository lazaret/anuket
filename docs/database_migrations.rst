Database migrations
*******************

During the process of writing an application it's often necessary to
modify and extend the database structure. To allow this, Anuket integrate
the Alembic_ package witch work with SQLAlchemy.

To migrate your database, you can use the ``upgrade_anuket_db`` script provided
with Anuket:

.. code-block:: text

    $ upgrade_anuket_db development.ini


or the alembic command:

.. code-block:: text

    $ alembic -c development.ini -n app:main upgrade head

The only direrence is than the first one will check if you have a database
backup before performing the update.


.. warning:: SQLite have limitaions with the ALTER statement and so Alembic do
    not support well tables and columns alteration of SQLite databases.


.. _Alembic: http://pypi.python.org/pypi/alembic
