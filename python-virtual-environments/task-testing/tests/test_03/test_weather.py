import requests
import pytest
import os
import re

from weather_03.weather_wrapper import WeatherWrapper, BASE_URL, FORECAST_URL



@pytest.fixture(scope='module')
def weather_wrapper_instance():
	print('------------------>   setUp')
	yield WeatherWrapper('44d4571d7871f56e5325ee4253f44fa9')
	print('------------------>   tearDown')


def test_get(weather_wrapper_instance):
	assert isinstance(weather_wrapper_instance.get('London', BASE_URL), requests.Response)


def test_get_response_city(weather_wrapper_instance):
	with pytest.raises(AttributeError):
		weather_wrapper_instance.get_response_city('London!', BASE_URL)

	assert isinstance(weather_wrapper_instance.get_response_city('London', BASE_URL), dict)


def test_get_temperature(weather_wrapper_instance):
	temperature = weather_wrapper_instance.get_temperature('London')
	assert isinstance(temperature, float)
	assert -100 < temperature < 60

def test_get_tomorrow_temperature(weather_wrapper_instance):
	temperature = weather_wrapper_instance.get_tomorrow_temperature('London')
	assert isinstance(temperature, float)
	assert -100 < temperature < 60


def test_find_diff_two_cities(weather_wrapper_instance):
	assert isinstance(weather_wrapper_instance.find_diff_two_cities('London', 'Paris'), float)


def test_get_diff_string(weather_wrapper_instance):
	diff_str = weather_wrapper_instance.get_diff_string('Dublin', 'Cairo')
	diff = weather_wrapper_instance.get_temperature('Dublin') - weather_wrapper_instance.get_temperature('Cairo')
	if diff < 0:
		diff = -diff
	diff = int(diff)
	assert diff_str == f"Weather in Dublin is colder than in Cairo by {diff} degrees"

	diff_str = weather_wrapper_instance.get_diff_string('Cairo', 'Dublin')
	diff = weather_wrapper_instance.get_temperature('Cairo') - weather_wrapper_instance.get_temperature('Dublin')
	if diff < 0:
		diff = -diff
	diff = int(diff)
	assert diff_str == f"Weather in Cairo is warmer than in Dublin by {diff} degrees"


def test_get_tomorrow_diff(weather_wrapper_instance):
	assert bool(re.fullmatch(r'The weather in \w+ tomorrow will be \w+ than today' , weather_wrapper_instance.get_tomorrow_diff('London')))


