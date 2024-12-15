import inspect
import itertools
from functools import partial
import pytest


def parametrized(func, combine=None, **kwargs):
    """Decorate a function with combined parameters."""
    argspec = inspect.getfullargspec(func)
    params = dict(zip(reversed(argspec.args), reversed(argspec.defaults)))
    func.__defaults__ = ()  # pytest ignores params with defaults
    if combine is None and len(params) > 1:
        raise ValueError("multiple keywords require combine function, e.g., zip")
    if combine not in (None, itertools.product):
        params = {','.join(params): combine(*params.values())}
    for param in params.items():
        func = pytest.mark.parametrize(*param, **kwargs)(func)
    return func


def fixture(*params, **kwargs):
    return pytest.fixture(params=params, **kwargs)(lambda request: request.param)


parametrized.fixture = fixture
parametrized.zip = partial(parametrized, combine=partial(zip, strict=True))
parametrized.product = partial(parametrized, combine=itertools.product)
