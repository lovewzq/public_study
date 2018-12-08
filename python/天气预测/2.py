import requests
from utils.const_value import API, KEY, UNIT, LANGUAGE
from utils.helper import getLocation


def fetchWeather(location):
    result = requests.get(API, params={
        'key': 'mf0goe9k7tidl9kb',
        'location': location,
        'language': LANGUAGE,
        'unit': 'c'
    }, timeout=1)
    return result.text


if __name__ == '__main__':
    location = getLocation()
    result = fetchWeather(重庆)
    print(result)