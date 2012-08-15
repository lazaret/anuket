Anuket
******

Anuket is an opinionated Python web framework based on Pyramid_. It is intended
to be used by other Pyramid applications as a base for common choices. Anuket
use URLDispatch for resources location, SQLAlchemy for ORM, Mako and Twitter
Bootstrap for templates.

----------

Documentation
=============
The full documentation is available at `Read the Docs`_.


Installation
------------
In short::

    $ pip install anuket

This will install Anuket and all the necessary Python packages dependencies.
For more detailed instructions please read the INSTALL.txt file.


Usage
-----
Anuket is write so he can be extended by other Pyramid applications by using
the extensibility system of Pyramid. For details please read the
`Anuket tutorial`_.

Licence
=======
Anuket is provided under the Expat licence (or MIT licence). See the
LICENSE.txt file for details.


Authors
=======
Anuket is maintained by the `Lazaret laboratory`_. See the
AUTHORS.txt file for the full list.


Development
===========
Contributions to Anuket are highly welcome. Please use Github to report bugs,
feature requests and submit your code:
https://github.com/lazaret/anuket

Note that development is done on the *develop* branch. The *master* is reserved
for production-ready state. Therefore make sure to base your work on the
*develop* branch.

.. image:: https://secure.travis-ci.org/lazaret/anuket.png
   :target: http://travis-ci.org/lazaret/anuket


.. _Anuket tutorial: http://anuket.readthedocs.org/en/latest/anuket_tutorial.html

.. _Lazaret laboratory: http://lazaret.unice.fr/
.. _Pyramid: http://pylonsproject.org/
.. _Read the Docs: http://anuket.readthedocs.org/
