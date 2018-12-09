import json
import os

T=['今天','明天','后天','大后天','大大后天']
txt=['会理','德阳','重庆']

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
    #print(city+"的天气信息如下：")
    #print("")
    #print(T[i]+Day+Week)
    #print("天气类型："+Type)
    #print("最"+High)
    #print("最"+Low)
    #print("平均温度："+wd)
    #print("湿度："+sd)
    #print("日出时间："+Sunrise)
    #print("日落时间："+Sunrset)
    #print(Fx)
    #print("风速："+Fs)
    #print("小贴士："+Notice)
    #print("")
    #print("---------------------")
    #print("")

    Text=city+'的天气信息如下：\r\n\r\n'+T[i]+Day+Week+"\r\n天气类型："+Type+"\r\n最"+High+"\r\n最"+Low+"\r\n平均温度："+wd+"\r\n湿度："+sd+"\r\n日出时间："+Sunrise+"\r\n日落时间："+Sunrset+"\r\n"+Fx+"\r\n风速："+Fs+"\r\n\r\n小贴士："+Notice+"\r\n-------------------"+"\r\n\r\n"

    return Text

#读取json文件数据
for i in range(3):         #总循环次数
    for j in range(3):      #每次读取三个文件
        os.chdir('F:\Git\public_study\python\自动邮件天气预报\DATA\JSON')
        with open(txt[i]+'.json', 'rb') as f:
            content = f.read().decode('utf-8')

#将json数据放入字典
            chushi = json.loads(content)
#获取并分离大字典的天气数据
            data=chushi['data']
#分离地点信息
            City=chushi['cityInfo']
            city=City['city']

    #今天的湿度
            sd=data['shidu']

    #今天的平均温度
            wd=data['wendu']

    #获取未来几天的天气信息
            dataa=data['forecast']
    #今天

        #for j in range(5):
            #data[j]=dataa[j]
            #info(data[j])

for a in range(3):
    for b in range(3):
        try:
            data[b]=dataa[b]
            print(info(data[b]))
            os.chdir('F:\Git\public_study\python\自动邮件天气预报\DATA\TXT') 
            f = open(txt[b]+'.txt', 'w', encoding='utf-8')
            f.write(info(data[b]))#打开weather.json后直接写入json串
            f.close()
            #print("数据写入成功！！")
        except:
            print("数据写入失败！！")








