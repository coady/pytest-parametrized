.. image:: https://img.shields.io/pypi/v/parametrized.svg
   :target: https://pypi.python.org/pypi/parametrized/
.. image:: https://img.shields.io/pypi/pyversions/parametrized.svg
.. image:: https://img.shields.io/pypi/status/parametrized.svg
.. image:: https://img.shields.io/travis/coady/parametrized.svg
   :target: https://travis-ci.org/coady/parametrized
.. image:: https://img.shields.io/codecov/c/github/coady/parametrized.svg
   :target: https://codecov.io/github/coady/parametrized

Pytest plugin for parametrizing tests with default iterables,
providing alternative syntax for pytest.mark.parametrize.

Usage
=========================

.. code-block:: python

   @pytest.parametrized
   def test(name=values, ...)
      """test single parametrized arg with each value"


   @pytest.parametrized.zip
   def test(name=values, name1=values1, ...)
      """test parametrized args with zipped values"

   @pytest.parametrized.product
   def test(name=values, name1=values1, ...)
      """test parametrized args with cartesian product of values"

Installation
=========================
::

   $ pip install pytest-parametrized

Dependencies
=========================
* Python 2.7, 3.4+

Tests
=========================
100% branch coverage. ::

   $ pytest [--cov]
