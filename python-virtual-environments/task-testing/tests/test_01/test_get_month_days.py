import pytest

from simple_library_01.functions import get_month_days


def test_get_month_days():
	assert 30 == get_month_days(1930, 1)

	assert 29 == get_month_days(2024, 2)
	assert 28 == get_month_days(2022, 2)

	with pytest.raises(AttributeError):
		get_month_days(2022, 13)

	assert 30 == get_month_days(2022, 4)

	assert 31 == get_month_days(2022, 5)
