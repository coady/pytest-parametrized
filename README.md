[![image](https://img.shields.io/pypi/v/pytest-parametrized.svg)](https://pypi.org/project/pytest-parametrized/)
[![image](https://img.shields.io/pypi/pyversions/pytest-parametrized.svg)](https://python3statement.org)
![image](https://img.shields.io/pypi/status/pytest-parametrized.svg)
[![image](https://img.shields.io/travis/coady/pytest-parametrized.svg)](https://travis-ci.org/coady/pytest-parametrized)
[![image](https://img.shields.io/codecov/c/github/coady/pytest-parametrized.svg)](https://codecov.io/github/coady/pytest-parametrized)
[![image](https://requires.io/github/coady/pytest-parametrized/requirements.svg)](https://requires.io/github/coady/pytest-parametrized/requirements/)
[![image](https://api.codeclimate.com/v1/badges/2abbe9cb6925b77018d6/maintainability)](https://codeclimate.com/github/coady/pytest-parametrized/maintainability)

[Pytest plugin](https://docs.pytest.org/en/latest/plugins.html) for parametrizing tests with default iterables,
providing alternative syntax for [pytest.mark.parametrize](https://docs.pytest.org/en/latest/parametrize.html).

# Usage
Decorate tests with iterable default values.

## functions
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

Zip before and after example:
```python
@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 42),
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

@pytest.parametrized.zip
def test_eval(test_input=("3+5", "2+4", "6*9"), expected=(8, 6, 42)):
    assert eval(test_input) == expected
```

Product before and after example:
```python
@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    pass

@pytest.parametrized.product
def test_foo(x=(0, 1), y=(2, 3)):
    pass
```

## fixtures
[Parametrized fixtures](https://docs.pytest.org/en/latest/fixture.html#fixture-parametrize) which simply return their param.

```python
fixture_name = pytest.parametrized.fixture(*params, **kwargs)
```

Before and after example:
```python
@pytest.fixture(params=[0, 1], ids=["spam", "ham"])
def a(request):
    return request.param

a = pytest.parametrized.fixture(0, 1, ids=["spam", "ham"])
```

# Installation

    $ pip install pytest-parametrized

Require plugin as usual in [conftest.py](https://docs.pytest.org/en/latest/plugins.html#requiring-loading-plugins-in-a-test-module-or-conftest-file).

```python
pytest_plugins = 'parametrized', ...
```

# Tests
100% branch coverage.

    $ pytest [--cov]

# Changes
1.0
* `parametrized` keyword options

0.2
* `fixture` keyword options
