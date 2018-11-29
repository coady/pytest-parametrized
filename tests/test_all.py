import pytest
data = pytest.parametrized.fixture('one', 'two')


def test_options():
    fixture = pytest.parametrized.fixture(name='override')
    assert fixture._pytestfixturefunction.name == 'override'
    assert pytest.parametrized(lambda x='': x, scope='module').kwargs == {'scope': 'module'}


def test_fixture(data):
    assert data in ('one', 'two')


@pytest.parametrized
def test_single(name='abc'):
    assert name in set('abc')


@pytest.parametrized.zip
def test_zip(name='abc', value=range(3)):
    assert (value, name) in enumerate('abc')


@pytest.parametrized.product
def test_product(name='abc', value=range(3)):
    assert name in set('abc') and value in (0, 1, 2)


def test_error(name='abc', value=range(3)):
    with pytest.raises(ValueError):
        @pytest.parametrized
        def test(name=(), value=()):
            pass
