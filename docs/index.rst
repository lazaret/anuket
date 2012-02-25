
========
Wepwawet
========

:Version: 0.1a, released XXXX-XX-XX
:Source: https://bitbucket.org/miniwark/wepwawet (Git)


:app:`Wepwawet` is an opiniated web framework based on Pyramid_. It is intended
to be used by other Pyramid projects as a base for common choices.

Choices done for you by Wepwawet :
* URLDispatch: Resources location mecanism
* SQLAlchemy_: SQL toolkit and ORM
* Formencode_: Forms validator
* Mako_: Templating engine
* `Twitter Bootstrap`_: Default templates

The project will also probably integrate :
* Alembic_: SQLAlchemy migration toolkit
* `Ziggurat foundations`_: SQLAlchemy classes for Auth & Auth

The developement is still at a very early stage and other choices have to be
made before the 0.2 version. In particulary take care of the facts :
* The database schema is subject to change
* Colander may be choised over Formencode for forms validation
* A password checker have to be choised. Probably ctypescracklib or Pwtools.
* A database versioning mecanism may be integrated too


Usage
=====
`Wepwawet` is writed so he can be extended by your Pyramid project. Normaly,
it is not necessary to fork Wepwawet. Just use the extensibility mecanism. For
details please read the Pyramid documentation :
http://docs.pylonsproject.org/projects/pyramid/en/1.3-branch/narr/extending.html


Authors
=======
.. literalinclude:: ..AUTHORS.txt

Roadmap
=======
.. literalinclude:: ..TODO.txt

License
=======
.. literalinclude:: ..LICENSE.txt


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
