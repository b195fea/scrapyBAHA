import scrapy

# https://forum.gamer.com.tw/B.php?bsn=31066
from scrapy import Selector
from selenium import webdriver
from scrapy.http import Request, FormRequest

class gammerSpider(scrapy.Spider):
    name = "bh3"
    allowes_domains = ["forum.gamer.com.tw"]
    start_urls = ('https://forum.gamer.com.tw/B.php?bsn=31066',)

    def __init__(self):
         self.driver = webdriver.chrome

    # 標籤頁
    def parse(self, response):
        # urls = response.css('a[class=b-list__main__title]').extract()

        # 爬自己網頁 下一頁
        next_page_url = response.xpath('//a[@class="b-list__main__title"]/@href').extract_first()
        url = response.urljoin(next_page_url)
        if url:
            yield scrapy.Request(url, callback=self.parseContent)

        # next_page_url = response.xpath('//a[@class="b-list__main__title"]/@href').extract()
        # for next in next_page_url:
        #     url = response.urljoin(next)
        #     # print(url)
        #     if url:
        #         yield scrapy.Request(url, callback=self.parseContent)

        # 爬自己網頁 下一頁
        # next_page_url = response.xpath('//a[@class="next"]/@href').extract_first()
        # url = response.urljoin(next_page_url)
        # if url:
        #     yield scrapy.Request(url, callback=self.parse)

    # 抓取頁面內容
    def parseContent(self, response):
        # print(response.body)
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # 取得標題
        title = response.selector.xpath('//h1[@class="title"]/text()').get()
        # 取得內文
        content = response.selector.xpath('//div[@class="c-article__content"]/*/text()').getall()
        # 取得作者
        floor = response.selector.xpath('//div[@class="c-post__header__author"]/a[1]/text()').getall() # 樓主
        authorName = response.selector.xpath('//div[@class="c-post__header__author"]/a[2]/text()').getall() # 作者中文
        authorId = response.selector.xpath('//div[@class="c-post__header__author"]/a[3]/text()').getall() # 作者ID
        # 取得日期時間
        time = response.selector.xpath('//div[@class="c-post__header__info"]/*/text()').getall()
        # 取得下一頁

        # content = response.xpath('//div[@class="c-article__content"]/text()').extract_first()
        # print(' content --------------------------------------------------')
        # for data in content:
        #     print('data： ' + data)
        #
        # # print(content)
        # print('content --------------------------------------------------')
        #
        # print(' author --------------------------------------------------')
        # for data in floor:
        #     print('floor： ' + data)
        #
        # for data in authorName:
        #     print('authorName： ' + data)
        #
        # for data in authorId:
        #     print('authorId： ' + data)
        #
        # for data in time:
        #     print('time： ' + data)

        # print(content)
        # 下一頁
        #
        # next_page_url = response.xpath('//a[@class="next"]/@href').extract_first()
        # url = response.urljoin(next_page_url)
        # if url:
        #     yield scrapy.Request(url, callback=self.parseContent)







        # -----------------------------------------------下面廢棄---------------------------------------------------------------
        # text = response.xpath("/html/head/title/text()")
        # print(text)

        # for url in urls:
        #     yield Request(url, callback=self.parse_lyrics)

        # if next_page:
        #     next_href = next_page[0]
        #     next_page_url = 'https://forum.gamer.com.tw' + next_href
        #     request = scrapy.Request(url=next_page_url)
        #     yield request
        #
        # next = self.driver.find_element_by_css_selector('a[class=b-list__main__title]')
        # # self.driver.get('https://forum.gamer.com.tw/B.php?bsn=31066')
        # text = response.xpath("/html/head/title/text()")
        # content = Selector(response=response).css('a[class=b-list__main__title]').getall()

        # content = response.css('div[class=b-list__main__title]')
        #

        # content = '/html[1]/body[1]/div[5]/div[1]/div[2]/form[1]/div[1]/table[1]/tbody[1]/tr[8]/td[2]/a[1]/div[2]/div[1]/p[1]'
        # content = '//p'
        # text3 = Selector(response=response).xpath(content + '/text()').getall()
        # text = response.xpath("//form[@name='formm']")

        # print('start ----------------------------------------------------------------------------------')
        # print(text)
        # print(content)
        # # print(text3)
        # print('end   ----------------------------------------------------------------------------------')


#
# class MyfirstpjtItem(scrapy.Item):
#     name = scrapy.Field()
#
#
# class northshoreSpider(scrapy.Spider):
#     name = 'xxx'
#     allowed_domains = ['www.example.org']
#     start_urls = ['https://www.example.org']
#
#     def __init__(self):
#      self.driver = webdriver.Firefox()
#
#     def parse(self,response):
#       self.driver.get('https://www.example.org/abc')
#
#       while True:
#        try:
#         next = self.driver.find_element_by_xpath('//*[@id="BTN_NEXT"]')
#         url = 'http://www.example.org/abcd'
#         yield Request(url,callback=self.parse2)
#         next.click()
#        except:
#         break
#
#       self.driver.close()
#
#     def parse2(self,response):
#      print 'you are here!'



 # def parse(self, response):
 #        self.driver.get('https://forum.gamer.com.tw/B.php?bsn=31066')
 #        text = response.xpath("/html/head/title/text()")
 #        text2 = response.xpath("/html[1]/body[1]/div[6]/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/span[2]/a/text()")
 #        text3 = Selector(response=response).xpath('//a/text()').getall()
 #        text = response.xpath("//form[@name='formm']")
 #        body = '<html><body><span>good</span></body></html>'
 #        body = '''
 #        <html>
 #            <head>
 #          <base href='http://example.com/' />
 #          <title>Example website</title>
 #         </head>
 #         <body>
 #          <div id='images'>
 #           <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' /></a>
 #           <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' /></a>
 #           <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' /></a>
 #           <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' /></a>
 #           <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>
 #          </div>
 #         </body>
 #        </html>
 #        '''
 #        text4 = Selector(text=body).xpath('//a/text()').getall()
 #        print('----------------------------------------------------------------------------------')
 #        print(text)
 #        print(text2)
 #        print(text3)
 #        print(text4)
 #        print('1111111111111111111111111111111111111111111111')
