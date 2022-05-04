
import pytest
from physical.week_number import get_count_weeks_year
from datetime import date


@pytest.mark.parametrize(
    'test_date, expected', [
        ((2021, 9, 24), 39),
        ((2022, 6, 12), 25),
        ((2019, 1, 5), 1),
        ((2019, 1, 6), 2),
    ]
)
def test_get_count_weeks_year(test_date, expected):
    year, month, day = test_date
    assert get_count_weeks_year(date(year, month, day)) == expected
