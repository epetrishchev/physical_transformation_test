
import pytest
from physical.week_number import get_total_count_weeks
from datetime import date


@pytest.mark.parametrize(
    'test_date, expected', [
        ((2021, 9, 24), 145),
        ((2022, 9, 24), 198),
        ((2019, 1, 5), 1),
        ((2019, 1, 6), 2),
    ]
)
def test_total_count_weeks(test_date, expected):
    year, month, day = test_date
    assert get_total_count_weeks(date(year, month, day)) == expected
