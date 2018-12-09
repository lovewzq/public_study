import json
import os

T=['今天','明天','后天','大后天','大大后天']
txt=['会理','德阳','重庆']

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
    Text=city+'的天气信息如下：\r\n\r\n'+T[j]+Day+Week+"\r\n天气类型："+Type+"\r\n最"+High+"\r\n最"+Low+"\r\n平均温度："+wd+".0℃"+"\r\n湿度："+sd+"\r\n日出时间："+Sunrise+"\r\n日落时间："+Sunrset+"\r\n"+Fx+"\r\n风速："+Fs+"\r\n\r\n小贴士："+Notice+"\r\n-------------------"+"\r\n"

    return Text


for i in range(3):      #每次读取三个文件
    os.chdir('F:\Git\public_study\python\自动邮件天气预报\DATA\JSON')
    with open(txt[i]+'.json', 'rb') as f:
        content = f.read().decode('utf-8')
        chushi = json.loads(content)
        data=chushi['data']
        City=chushi['cityInfo']
        city=City['city']
        sd=data['shidu']
        wd=data['wendu']
        dataa=data['forecast']

        for j in range(5):
            data[j]=dataa[j]
            text=info(data[j])
            try:
                os.chdir('F:\Git\public_study\python\自动邮件天气预报\DATA\TXT')
                f = open(txt[i]+'.txt', 'a+', encoding='utf-8')
                f.write(text)#打开weather.json后直接写入json串
                f.close()
                print("数据写入成功！！")
            except:
                print("数据写入失败！！")