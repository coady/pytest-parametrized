from textwrap import dedent

import pytest
from parametrized import parametrized

data = parametrized.fixture('one', 'two')


def test_options():
    fixture = parametrized.fixture(name='override')
    assert fixture._pytestfixturefunction.name == 'override'
    assert parametrized(lambda x='': x, scope='module').kwargs == {'scope': 'module'}


def test_fixture(data):
    assert data in ('one', 'two')


@parametrized
def test_single(name='abc'):
    assert name in set('abc')


@parametrized.zip
def test_zip(name='abc', value=range(3)):
    assert (value, name) in enumerate('abc')


@parametrized.product
def test_product(name='abc', value=range(3)):
    assert name in set('abc') and value in (0, 1, 2)


def test_error(name='abc', value=range(3)):
    with pytest.raises(ValueError):

        @parametrized
        def test(name=(), value=()):
            pass


@parametrized.product
def test_param(key=[0], value=[0, pytest.param(1, marks=pytest.mark.xfail())]):
    assert key == value


def test_zip_strict_error(tmp_path, capsys):
    unrunnable_test_file = tmp_path / "test_zip_strict_error.py"

    unrunnable_test_file.write_text(
        dedent(
            """
            from parametrized import parametrized

            @parametrized.zip_strict
            def test_zip_strict_error(name='abc', value=range(4)):
                pass
            """
        ).lstrip()
    )

    exit_code = pytest.main([str(unrunnable_test_file)])
    assert exit_code == pytest.ExitCode.INTERRUPTED
    assert "ValueError: zip() argument 2 is shorter than argument 1" in capsys.readouterr().out
