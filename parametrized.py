import inspect
import itertools
from functools import partial
import pytest

__version__ = '0.1'


def parametrized(func, combine=None):
    """Decorate a function with combined parameters."""
    if hasattr(inspect, 'signature'):
        params = inspect.signature(func).parameters.items()
        params = {name: param.default for name, param in params if param.default != param.empty}
    else:  # py2
        argspec = inspect.getargspec(func)
        params = dict(zip(reversed(argspec.args), reversed(argspec.defaults)))
    func.__defaults__ = ()  # pytest ignores params with defaults
    if combine is None:
        args, = params.items()  # multiple keywords require combine function, e.g., zip
    else:
        args = ','.join(params), combine(*params.values())
    return pytest.mark.parametrize(*args)(func)


def fixture(*params):
    return pytest.fixture(params=params)(lambda request: request.param)


parametrized.fixture = fixture
parametrized.zip = partial(parametrized, combine=zip)
parametrized.product = partial(parametrized, combine=itertools.product)


def pytest_namespace():
    return {'parametrized': parametrized}
