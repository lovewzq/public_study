import requests
import json

url='http://t.weather.sojson.com/api/weather/city/'

f = open('F:\Git\public_study\python\自动邮件天气预报\weather.json', 'w', encoding='utf-8')

def fetchWeather(location):
    result = requests.get(url+location)
    return result.text

if __name__ == '__main__':
    result = fetchWeather('101272001')
    
    #names = json.dumps(result,ensure_ascii=False,encoding='utf-8')
    f.write(result)#打开weather.json后直接写入json串
    print(result)