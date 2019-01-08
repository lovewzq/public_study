# -*- coding: utf-8 -*-

import scrapy


class MainSpider(scrapy.Spider):
    name="spider5"

    def start_requests(self):
        url="http://space.bilibili.com/"

        for i in range(2):
            url=url+str(i)
        yield scrapy.Request(url, self.parse)
        
    def parse(self, response):
        if response.status == 200:
            with open("01.txt", "a+") as f:
                f.write(response.body)
                f.close()
