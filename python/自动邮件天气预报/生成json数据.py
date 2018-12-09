import requests
import json
import os

#API地址
url='http://t.weather.sojson.com/api/weather/city/'

#城市列表
#会理：101271606
#德阳：101272001
#沙坪坝：101043700

city=['101271606','101272001','101040100']
txt=['会理','德阳','重庆']


def fetchWeather(location):
    result = requests.get(url+location)
    return result.text

for i in range(3):
    result = fetchWeather(city[i])
    os.chdir('F:\Git\public_study\python\自动邮件天气预报\DATA\JSON') 
    f = open(txt[i]+'.json', 'w', encoding='utf-8')
    f.write(result)#打开weather.json后直接写入json串
    f.close()
    #print(result)