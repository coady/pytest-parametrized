.. image:: https://img.shields.io/pypi/v/pytest-parametrized.svg
   :target: https://pypi.python.org/pypi/pytest-parametrized/
.. image:: https://img.shields.io/pypi/pyversions/pytest-parametrized.svg
.. image:: https://img.shields.io/pypi/status/pytest-parametrized.svg
.. image:: https://img.shields.io/travis/coady/pytest-parametrized.svg
   :target: https://travis-ci.org/coady/pytest-parametrized
.. image:: https://img.shields.io/codecov/c/github/coady/pytest-parametrized.svg
   :target: https://codecov.io/github/coady/pytest-parametrized

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
