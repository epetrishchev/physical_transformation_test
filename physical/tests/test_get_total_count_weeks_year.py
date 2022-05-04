
import pytest
from physical.week_number import get_total_count_weeks_year


@pytest.mark.parametrize(
    'test_year, expected', [
        (2021, 53),
        (2022, 53),
        (2023, 54),
        (2024, 53),
    ]
)
def test_get_total_count_weeks_year(test_year, expected):
    assert get_total_count_weeks_year(test_year) == expected
