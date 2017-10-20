.. image:: https://img.shields.io/pypi/v/pytest-parametrized.svg
   :target: https://pypi.python.org/pypi/pytest-parametrized/
.. image:: https://img.shields.io/pypi/pyversions/pytest-parametrized.svg
.. image:: https://img.shields.io/pypi/status/pytest-parametrized.svg
.. image:: https://img.shields.io/travis/coady/pytest-parametrized.svg
   :target: https://travis-ci.org/coady/pytest-parametrized
.. image:: https://img.shields.io/codecov/c/github/coady/pytest-parametrized.svg
   :target: https://codecov.io/github/coady/pytest-parametrized

`Pytest plugin`_ for parametrizing tests with default iterables,
providing alternative syntax for `pytest.mark.parametrize`.

Usage
=========================
Decorate tests with iterable default values.

.. code-block:: python

   @pytest.parametrized
   def test(name=values, ...):
      """test single parametrized arg with each value"""

   @pytest.parametrized.zip
   def test(name=values, name1=values1, ...):
      """test parametrized args with zipped values"""

   @pytest.parametrized.product
   def test(name=values, name1=values1, ...):
      """test parametrized args with cartesian product of values"""

Simple parametrized fixtures also supported, for easier reuse.

.. code-block:: python

   fixture_name = pytest.parametrized.fixture(*params)

Installation
=========================
::

   $ pip install pytest-parametrized

Require plugin as usual in `conftest.py`.

.. code-block:: python

   pytest_plugins = 'parametrized', ...

Dependencies
=========================
* Python 2.7, 3.4+

Tests
=========================
100% branch coverage. ::

   $ pytest [--cov]

.. _Pytest plugin: https://docs.pytest.org/en/latest/plugins.html
