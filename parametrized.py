import inspect
import itertools
from functools import partial
import pytest

__version__ = '1.4'


def parametrized(func, combine=None, **kwargs):
    """Decorate a function with combined parameters."""
    argspec = inspect.getfullargspec(func)
    params = dict(zip(reversed(argspec.args), reversed(argspec.defaults)))
    func.__defaults__ = ()  # pytest ignores params with defaults
    if combine is None:
        (args,) = params.items()  # multiple keywords require combine function, e.g., zip
    else:
        args = ','.join(params), combine(*params.values())
    return pytest.mark.parametrize(*args, **kwargs)(func)


def fixture(*params, **kwargs):
    return pytest.fixture(params=params, **kwargs)(lambda request: request.param)


parametrized.fixture = fixture
parametrized.zip = partial(parametrized, combine=zip)
parametrized.product = partial(parametrized, combine=itertools.product)
