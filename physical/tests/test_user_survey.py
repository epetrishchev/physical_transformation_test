
import pytest
from physical.week_number import user_survey
from io import StringIO


@pytest.mark.parametrize(
    'test_input, expected', [
        ('да\n', False),
        ('дА\n', False),
        ('Да\n', False),
        ('yes\n', False),
        ('Yes\n', False),
        ('yEs\n', False),
        ('yeS\n', False),
        ('нет\n', True),
        ('Нет\n', True),
        ('нЕт\n', True),
        ('неТ\n', True),
        ('no\n', True),
        ('No\n', True),
        ('nO\n', True),
    ]
)
def test_user_survey(monkeypatch, test_input, expected):
    input = StringIO(test_input)
    monkeypatch.setattr('sys.stdin', input)
    assert user_survey() == expected
