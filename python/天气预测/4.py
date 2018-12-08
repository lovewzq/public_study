import requests

url='https://www.tianqiapi.com/api'

city='101043800'


def fetchWeather(location):
    result = requests.get(url,city, timeout=1,verify=False)
    return result.text


if __name__ == '__main__':
    result = fetchWeather('WK8XWZ0HJ8Q4')
    print(result)