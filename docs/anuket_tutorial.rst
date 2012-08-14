Tutorial
********

This tutorial will explain the course to create an 'Hello world' application
with Anuket.

Introduction
============

Anuket is a python application based on the Pyramid_ web framework. Anuket is
intended to provide features not bundled by Pyramid. The main features
provided by Anuket are:

* `Twitter Bootstrap`_ template
* Form management
* Flash messages
* Database based Users & groups
* Database migrations
* Admin tools backend

The main objective of Anuket, is to be used for relational database driven
applications. For example, application with web forms, or wikis.

During this tutorial, we will create a very simple 'Hello world' application.
You can browse the code of this example application in our Git repository :
https://github.com/lazaret/anuket-example


Install Anuket and the prerequistes
===================================

Anuket require the Python language (2.7 version), and a SQL database engine. In
this tutorial we will use SQLite.

For this tutorial we will asume than they are already installed on your
computer. If it's not the case, please install them.


Prepare the isolated environment
--------------------------------

To avoid messing with your working Python environment during this tutorial, we
will create first an an isolated environment:

.. code-block:: text

    $ easy_install virtualenv
    $ virtualenv --no-site-packages tutorial
    $ source tutorial/bin/activate

This, have:

* installed the virtualenv_ and pip_ packages
* activated the `tutorial` isolated environment

When you will have finish the tutorial, you can get rid of everything we done
by just deleting the /tutorial directory.


Install Anuket
--------------

You can simply install Anuket from PyPI by using `pip`, a Python packages
installer witch have been installed with `virtualenv` :

.. code-block:: text

    (tutorial)$ pip install anuket

This will install Anuket and all the required Python packages (`Pyramid`,
`SQLAlchemy`, `Mako`, `alembic`, etc.). You can display the list of all the
installed packages with `pip`:

.. code-block:: text

    (tutorial)$ pip freeze


Create the example application
==============================

TODO


Create the application
----------------------

We need first to create a Pyramid application with the `starter` scafold:

.. code-block:: text

    (tutorial)$ pcreate -t starter anuket-example

This create a minimalistic Pyramid application with all the default files. We
will edit this file to create our example application. In a future release we
will add ou own scafold to start with.


Configure the application
-------------------------

We need now to edit three files to tell the application to use Anuket as a
base:

* setup.py
* development.ini
* anuketexample/__init__.py


If your are lazy you can download them directly from
http://github.com/lazaret/anuket-example

First we need to tell to the ``setup.py`` file than ``anuket`` is a prerequiste
for our application:

.. literalinclude:: tutorial_setup.py
   :language: python
   :lines: 9-13
   :linenos:

Secondly we have to edit the ``development.ini`` to add the options required
by Anyket:

.. literalinclude:: tutorial_development.ini
   :language: ini
   :lines: 1-35
   :linenos:

Most notabily we have set with this options:

* The SQLAlchemy database type and name
* The Mako template engine options
* The Beaker session options
* Anuket options

Finaly we need to tell imperatively to our application than we will use Anuket.
For this will have to edit the ``__init__.py`` file inside the
``anuketexample`` directory.

.. literalinclude:: tutorial__init__.py
   :language: python
   :linenos:

In this file we have configured the database, the authentification, the
session, the routes, the view and even the translation mecanism. And as you can
see, most of them comme from Anuket.


Initialize the application
--------------------------

We need now to initialize the database for our application. For this we will
use the `initialize_anuket_db` script.

.. code-block:: text

    (tutorial)$ initialize_anuket_db development.ini

The script read the sqlalchemy.url option and our database model, then create
the database, and finaly fill it with default values.

As we use SQLite the script have normaly created a anuket-example.db file witch
is our database.


Serve the application
---------------------

At this point we have now a working application than we can serve:

. code-block:: text

    (tutorial)$ pserve develpment.ini

You can access to the application with a web browser at http://0.0.0.0:6543/

For now, the application only offer the base application from Anuket. You can
already login to the aplication with the default admin credentials:
admin/admin.


Add the `hello_world` view
--------------------------

Our starter application is ready. We now need to add features by extending the
application. For this we will add a wonderfull *Hello World* feature.
For this will have to edit the ``views.py`` file inside the ``anuketexample``
directory.


.. literalinclude:: tutorial_views.py
   :language: python
   :linenos:

This will create:

* The `include` function, with register the routes of the views when you lauch
the application with the `config.scan()` call.
* `Hello World` view available at http://0.0.0.0:6543/hello
* `Hello admin` view available at http://0.0.0.0:6543/hello/admin


Add the `hello.mako` template
-----------------------------

Our two views need a template to be rendered:

.. literalinclude:: tutorial_template.mako
   :language: python
   :linenos:

We use here a Mako template with inherit from the default templates of Anuket.
The template itsef just display the `hello` variable with is returned by the
views.


Connect to the views
--------------------

Now the application can serve the Anuket views and our two new views:

. code-block:: text

    (tutorial)$ pserve develpment.ini

You can for example the connect with your browser to:

===============================  =============  ===========
Adress                           View name      Application
===============================  =============  ===========
http://0.0.0.0:6543/             `home`         anuket
http://0.0.0.0:6543/hello        `hello`        anuket-example
http://0.0.0.0:6543/login        `login`        anuket
http://0.0.0.0:6543/hello/admin  `hello_admin`  anuket-example

Note than the `hello_admin` requiere an user with admin permission. If you try
to access to it without login first the application will redirect you to the
`login` view.


.. seealso:: `Creating your first Pyramid application`_


Further reading
===============

Anuket use the extensibility mecanism of Pyramid. To go further you will need
to read the `Pyramid documentation
<http://pyramid.readthedocs.org/en/1.3-branch/narr/extending.html>`_


.. _Pyramid: http://pylonsproject.org/
.. _pip: http://www.pip-installer.org/
.. _Twitter Bootstrap: http://twitter.github.com/bootstrap/
.. _virtualenv: http://www.virtualenv.org/

.. _Creating your first Pyramid application: http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/firstapp.html
