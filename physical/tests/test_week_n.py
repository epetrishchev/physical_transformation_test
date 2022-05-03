from pytest_mock import mocker

from physical.week_number import get_week_number


def test_get_week_number_1():
    with mocker.patch.object(__builtins__, 'input', lambda: '2021.09.24'):
        assert get_week_number() == 15
