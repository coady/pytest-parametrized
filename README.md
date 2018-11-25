[![image](https://img.shields.io/pypi/v/pytest-parametrized.svg)](https://pypi.org/project/pytest-parametrized/)
![image](https://img.shields.io/pypi/pyversions/pytest-parametrized.svg)
![image](https://img.shields.io/pypi/status/pytest-parametrized.svg)
[![image](https://img.shields.io/travis/coady/pytest-parametrized.svg)](https://travis-ci.org/coady/pytest-parametrized)
[![image](https://img.shields.io/codecov/c/github/coady/pytest-parametrized.svg)](https://codecov.io/github/coady/pytest-parametrized)
[![image](https://requires.io/github/coady/pytest-parametrized/requirements.svg)](https://requires.io/github/coady/pytest-parametrized/requirements/)
[![image](https://api.codeclimate.com/v1/badges/2abbe9cb6925b77018d6/maintainability)](https://codeclimate.com/github/coady/pytest-parametrized/maintainability)

[Pytest plugin](https://docs.pytest.org/en/latest/plugins.html) for parametrizing tests with default iterables,
providing alternative syntax for pytest.mark.parametrize.

# Usage
Decorate tests with iterable default values.

```python
@pytest.parametrized
def test(name=values, ...):
    """test single parametrized arg with each value"""

@pytest.parametrized.zip
def test(name=values, name1=values1, ...):
    """test parametrized args with zipped values"""

@pytest.parametrized.product
def test(name=values, name1=values1, ...):
    """test parametrized args with cartesian product of values"""
```

Simple parametrized fixtures also supported, for easier reuse.

```python
fixture_name = pytest.parametrized.fixture(*params)
```

# Installation

    $ pip install pytest-parametrized

Require plugin as usual in conftest.py.

```python
pytest_plugins = 'parametrized', ...
```

# Tests
100% branch coverage.

    $ pytest [--cov]

# Changes
0.2
* `fixture` keyword options
