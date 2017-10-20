import pytest


@pytest.parametrized
def test_single(name='abc'):
    assert name in set('abc')


@pytest.parametrized.zip
def test_zip(name='abc', value=range(3)):
    assert name in set('abc') and value in (0, 1, 2)


@pytest.parametrized.product
def test_product(name='abc', value=range(3)):
    assert name in set('abc') and value in (0, 1, 2)


def test_error(name='abc', value=range(3)):
    with pytest.raises(ValueError):
        @pytest.parametrized
        def test(name=(), value=()):
            pass
