Running tests
-------------

To run the tests, you need first to install the test packages
used to build the tests : :mod:`nose`, :mod:`WebTest`

.. code-block:: text
$ pip install tissue WebTest


Optionaly you can install the coverage package.

.. code-block:: text
$ pip install coverage


Then run the tests:

.. code-block:: text
$ python setup.py nostetests


Or simply:

.. code-block:: text
$ nostetests -v
