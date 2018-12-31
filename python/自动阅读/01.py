from splinter import Browser
browser = Browser('chrome')

while True:
    browser.visit('http://i.mooc.chaoxing.com/space/index?t=1545746200457')
    first=browser.find_by_xpath('/html/body/div/div[2]/div[2]/ul/li[1]/div[2]/h3/a').first


#browser.fill('wd', '时间')

