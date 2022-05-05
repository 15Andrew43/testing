from simple_library_01.functions import is_leap
from tree_utils_02.tree import Tree
from weather_03.weather_wrapper import WeatherWrapper

if __name__ == '__main__':
    print(is_leap(2021))

    print(Tree().get('./', dirs_only=False))
    token = '44d4571d7871f56e5325ee4253f44fa9'

    wrapper = WeatherWrapper(token)
    print(wrapper.get_temperature('London'))
