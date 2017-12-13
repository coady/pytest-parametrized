import inspect
import itertools
from functools import partial
import pytest

__version__ = '0.2'
getargspec = getattr(inspect, 'getfullargspec', inspect.getargspec)


def parametrized(func, combine=None):
    """Decorate a function with combined parameters."""
    argspec = getargspec(func)
    params = dict(zip(reversed(argspec.args), reversed(argspec.defaults)))
    func.__defaults__ = ()  # pytest ignores params with defaults
    if combine is None:
        args, = params.items()  # multiple keywords require combine function, e.g., zip
    else:
        args = ','.join(params), combine(*params.values())
    return pytest.mark.parametrize(*args)(func)


def fixture(*params, **kwargs):
    return pytest.fixture(params=params, **kwargs)(lambda request: request.param)


parametrized.fixture = fixture
parametrized.zip = partial(parametrized, combine=zip)
parametrized.product = partial(parametrized, combine=itertools.product)


def pytest_namespace():
    return {'parametrized': parametrized}
