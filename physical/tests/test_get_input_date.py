
from datetime import date
import pytest
from physical.week_number import get_input_date
from io import StringIO


@pytest.mark.parametrize(
    'test_input, expected', [
        ('2021.09.24\n', (2021, 9, 24)),
        ('2022.09.24\n', (2022, 9, 24)),
        ('2019.01.05\n', (2019, 1, 5)),
        ('2019.01.06\n', (2019, 1, 6)),
    ]
)
def test_get_input_date(monkeypatch, test_input, expected):
    input = StringIO(test_input)
    monkeypatch.setattr('sys.stdin', input)
    assert get_input_date() == expected
