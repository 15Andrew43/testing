import pytest

from simple_library_01.functions import is_leap


def test_is_leap():
	with pytest.raises(AttributeError):
		is_leap(0)

	assert True == is_leap(2000)
	assert False == is_leap(2100)
	assert False == is_leap(2001)
	