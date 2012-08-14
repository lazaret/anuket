Anuket
******
:Author: LDPL - Laboratoire Départemental de Préhistoire du Lazaret
:Version: 0.5b, released 2012-XX-XX
:PyPI:
:License: Expat license (MIT license)
:Docs: http://anuket.readthedocs.org/
:Source: https://github.com/lazaret/anuket (Git)
:Bugs: https://github.com/lazaret/anuket/issues


Introduction
============
**Anuket** is an opiniated Python web framework based on Pyramid_. It is
intended to be used by other Pyramid applications as a base for common choices.

Choices done for you by Anuket:

* Pyramid_: Core web framework
* URLDispatch: Resources location mecanism
* SQLAlchemy_: SQL toolkit and ORM
* FormEncode_: Form validator
* Pyramid_simpleform_: Form generator
* Mako_: Templating engine
* `Twitter Bootstrap`_: Default templates

The project also integrate:

* Alembic_: Database migration tool for SQLAlchemy
* Babel_: Internationalization and Localization tools
* Cracklib_: Password checking library
* Cryptacular_: Password hashing framework


Usage
=====
Anuket is writed so he can be extended by other Pyramid applications. Normaly,
it is not necessary to fork Anuket. Just use the extensibility mecanism. For
details please read the `Pyramid documentation
<http://pyramid.readthedocs.org/en/1.3-branch/narr/extending.html>`_

The main objective of Anuket, is to be used for database related
applications. We will use it at the `Lazaret laboratory`_ mostly for filling
and quering relational databases with web forms. If your application is like
this, Anuket may be suited for you.


Warning
=======
The developement is still at an early stage and other choices have to be
made before the 1.0 version. In particulary take care of the facts than:

* The database schema is subject to change
* WTForms may be choised over FormEncode and Pyramid_simpleform
* We may add a 'plugin' mecanism to allow optional features


Alternatives
============
There are already other web frameworks and CMS based on Pyramid. Anuket have
take  inspiration from them but the choices made are sometime different. They
may be best suited to your needs. Have a look on Akhet_, Apex_, Cone.app_,
Kotti_, Khufu_, Ptah_, PyCK_, Pyrone_ and more.


Narative documentation
======================

.. toctree::
   :maxdepth: 1

   install.rst
   anuket_tutorial.rst
   console_scripts.rst
   database_migrations.rst
   flash_messages.rst
   testing.rst
   authors.rst
   licenses.rst
   changes.rst
   todo.rst


API Documentation
==================

.. toctree::
   :maxdepth: 1

   api.rst


Index and Glossary
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. _Lazaret laboratory: http://lazaret.unice.fr/

.. _Alembic: http://pypi.python.org/pypi/alembic
.. _Babel: http://babel.edgewall.org/
.. _Cracklib: http://pypi.python.org/pypi/cracklib
.. _Cryptacular: http://pypi.python.org/pypi/cryptacular
.. _Formencode: http://www.formencode.org/
.. _Mako: http://www.makotemplates.org/
.. _Pyramid: http://pylonsproject.org/
.. _Pyramid_simpleform: http://packages.python.org/pyramid_simpleform/
.. _SQLAlchemy: http://www.sqlalchemy.org/
.. _Twitter Bootstrap: http://twitter.github.com/bootstrap/

.. _Akhet: http://pypi.python.org/pypi/Akhet
.. _Apex: http://thesoftwarestudio.com/apex/
.. _Cone.app: http://pypi.python.org/pypi/cone.app
.. _Kotti: http://pypi.python.org/pypi/Kotti
.. _Khufu: http://khufuproject.github.com/
.. _Ptah: http://pypi.python.org/pypi/ptah
.. _PyCK: http://pypi.python.org/pypi/PyCK
.. _Pyrone: http://pypi.python.org/pypi/pyrone
