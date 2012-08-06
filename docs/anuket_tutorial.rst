Anuket tutorial
***************

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
You can brownse the code of this example application in our Git repository :
https://github.com/lazaret/anuket-example


Install Anuket and the prerequistes
===================================

Anuket require the Python language (2.7 version), and a SQL database engine. In
this tutorial we will use sqlite3.

For this tutorial we will asume than they are already installed on your
computer. If it's not the case, please install them.


Prepare the isolated environment
--------------------------------

To avoid messing with your working Python environment during this tutorial, we
will create first an an isolated environment:

.. code-block:: text

    $ easy_install virtualenv
    $ virtualenv tutorial
    $ cd tutorial
    $ source /bin/activate

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
---------------------

TODO


Configure the application
-------------------------

TODO


Initialize the application
--------------------------

TODO


Add the `hello_world` view
--------------------------

TODO


Further reading
===============

Anuket use the extensibility mecanism of Pyramid. To go further you will need
to read the `Pyramid documentation
<http://pyramid.readthedocs.org/en/1.3-branch/narr/extending.html>`_


.. _Pyramid: http://pylonsproject.org/
.. _pip: http://www.pip-installer.org/
.. _Twitter Bootstrap: http://twitter.github.com/bootstrap/
.. _virtualenv: http://www.virtualenv.org/
