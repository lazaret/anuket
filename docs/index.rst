
========
Wepwawet
========

:Version: 0.1a, released XXXX-XX-XX
:Source: https://bitbucket.org/miniwark/wepwawet (Git)

Introduction
=======
**Wepwawet** is an opiniated Python web framework based on Pyramid_. It is intended
to be used by other Pyramid projects as a base for common choices.

Choices done for you by Wepwawet:

* Pyramid_: Core web framework
* URLDispatch: Resources location mecanism
* SQLAlchemy_: SQL toolkit and ORM
* Formencode_: Form validator
* Mako_: Templating engine
* `Twitter Bootstrap`_: Default template

The project will also probably integrate:

* Alembic_: SQLAlchemy migration toolkit
* `Ziggurat foundations`_: SQLAlchemy classes for Auth & Auth

Warning
=======
The developement is still at a very early stage and other choices have to be
made before the 0.2 version. In particulary take care of the facts than:

* The database schema is subject to change
* Colander may be choised over Formencode for forms validation
* A password checker have to be choised. Probably ctypescracklib or Pwtools.
* A database versioning mecanism may be integrated later


Usage
=====
Wepwawet is writed so he can be extended by your Pyramid project. Normaly,
it is not necessary to fork Wepwawet. Just use the extensibility mecanism. For
details please read the `Pyramid documentation 
<http://docs.pylonsproject.org/projects/pyramid/en/1.3-branch/narr/extending.html>`_


Alternatives
============
There are already other web frameworks and CMS based on Pyramid. Wepwawet have take 
inspiration from them but the choices made are sometime different. They may be best suited
to your project. Have a look on Akhet_, Apex_, Kotti_, Ptah_, PyCK_, Pyrone_.


.. include:: ../AUTHORS.txt


.. include:: ../TODO.txt


.. include:: ../LICENSE.txt


.. toctree::
   :maxdepth: 2

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. _Alembic: http://pypi.python.org/pypi/alembic
.. _Formencode: http://www.formencode.org/
.. _Mako: http://www.makotemplates.org/
.. _Pyramid: http://docs.pylonsproject.org/en/latest/docs/pyramid.html
.. _SQLAlchemy: http://www.sqlalchemy.org/
.. _Ziggurat foundations: https://bitbucket.org/ergo/ziggurat_foundations
.. _Twitter Bootstrap: http://twitter.github.com/bootstrap/

.. _Akhet: http://pypi.python.org/pypi/Akhet
.. _Apex: http://thesoftwarestudio.com/apex/
.. _Kotti: http://pypi.python.org/pypi/Kotti
.. _Ptah: http://pypi.python.org/pypi/ptah
.. _PyCK: http://pypi.python.org/pypi/PyCK
.. _Pyrone: http://pypi.python.org/pypi/pyrone