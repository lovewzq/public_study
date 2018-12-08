import json

T=['今天','明天','后天','大后天','大大后天']

#每日详细信息函数
def info(day):
    #获取信息
    Day=day['ymd']          #日期：YY-MM-DD
    Week=day['week']        #星期：
    Type=day['type']        #天气类型
    High=day['high']        #最高温度
    Low=day['low']          #最低温度
    Sunrise=day['sunrise']  #日出
    Sunrset=day['sunset']   #日落
    Fx=day['fx']            #风向
    Fs=day['fl']            #风速
    Notice=day['notice']    #小提示
    #输出信息
    print(T[i]+"是"+Day+Week)
    print("天气类型"+Type)
    print("最"+High)
    print("最"+Low)
    print("日出时间："+Sunrise)
    print("日落时间："+Sunrset)
    print(Fx)
    print("风速："+Fs)
    print("小贴士："+Notice)
    print("")
    print("---------------------")
    print("")



#读取json文件数据
with open('F:\Git\public_study\python\自动邮件天气预报\weather.json', 'rb') as f:
    content = f.read().decode('utf-8')

#将json数据放入字典
    chushi = json.loads(content)
#获取并分离大字典的数据

    data=chushi['data']

    #今天的湿度
    sd=data['shidu']

    #今天的平均温度
    wd=data['wendu']

    #获取未来几天的天气信息
    dataa=data['forecast']
    #今天

    for i in range(5):
        data[i]=dataa[i]
        info(data[i])
        









