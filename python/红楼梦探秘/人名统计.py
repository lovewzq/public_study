
#-*-coding:utf-8-*-    
import matplotlib.pyplot as plt  
from wordcloud import WordCloud  
import jieba  
  
text = open("红楼梦.txt","rb").read()  
#结巴分词  
mytext = jieba.cut(text,cut_all=False)  #采用精准模式，true为全模式
wt = " /".join(mytext)  
  
#设置词云  
wc = WordCloud(background_color = "black", #设置背景颜色  
               max_words = 1000, #设置最大显示的字数  
               font_path='C:\windows\Fonts\STZHONGS.TTF',#设置中文字体，词云默认字体是“DroidSansMono.ttf字体库”，不支持中文 
               max_font_size = 50,  #设置字体最大值  
               random_state = 30, #设置有多少种随机生成状态，即有多少种配色方案  
    )  
mycloud= wc.generate(wt)#生成词云  
  
#展示词云图  
plt.imshow(mycloud)  
plt.axis("off")  
plt.show()