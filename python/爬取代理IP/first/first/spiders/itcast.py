# -*- coding: utf-8 -*-
import scrapy

class Opp2Spider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/26752088/?tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&from=gaia_video']

    def parse(self, response):
        # 获取网站标题
        context = response.xpath('//*[@id="info"]/span[1]/span[2]/a')   
       
        # 提取网站标题
        title = context.extract_first()  
        print(title) 
        pass