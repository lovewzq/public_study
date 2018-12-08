import requests
#from utils.const_value import API, KEY, UNIT, LANGUAGE
#from utils.helper import getLocation

url='https://api.seniverse.com/v3/weather/now.json'

def fetchWeather(location):
    result = requests.get(url, params={
        'key': 'mf0goe9k7tidl9kb',
        'location': location,
        'language': 'zh-Hans',
        'unit': 'c'
    }, timeout=1,verify=False)
    return result.text


if __name__ == '__main__':
    result = fetchWeather('重庆')
    print(result)