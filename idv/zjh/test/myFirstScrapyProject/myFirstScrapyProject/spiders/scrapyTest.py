import scrapy

from scrapy import Selector
from selenium import webdriver
from idv.zjh.test.myFirstScrapyProject.myFirstScrapyProject.items import MyfirstscrapyprojectItem
from pypinyin import pinyin, lazy_pinyin, Style
from scrapy.http import Request, FormRequest

class gammerSpider(scrapy.Spider):
    name = "bh3"
    allowes_domains = ["forum.gamer.com.tw"]
    # 崩壞三 討論列表
    start_urls = ('https://forum.gamer.com.tw/B.php?bsn=31066',)

    def __init__(self):
        self.driver = webdriver.chrome

    # 標籤頁
    def parse(self, response):
        # urls = response.css('a[class=b-list__main__title]').extract()

        # 單頁面測試
        # next_page_url = response.xpath('//a[@class="b-list__main__title"]/@href').extract_first()
        # url = response.urljoin(next_page_url)
        # if url:
        #     yield scrapy.Request(url, callback=self.parseContent)

        # 全部爬蟲
        # 進入文章內容
        next_page_url = response.xpath('//a[@class="b-list__main__title"]/@href').extract()
        for next in next_page_url:
            url = response.urljoin(next)
            # print(url)
            if url:
                yield scrapy.Request(url, callback=self.parseContent)

        next_page_url = response.xpath('//p[@class="b-list__main__title"]/@href').extract()
        for next in next_page_url:
            url = response.urljoin(next)
            # print(url)
            if url:
                yield scrapy.Request(url, callback=self.parseContent)

        # 文章列表 下一頁
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

        # items = MyfirstscrapyprojectItem

        # 取得標題
        title = response.selector.xpath('//h1[@class="title"]/text()').get()
        # 取得內文
        # content = response.selector.xpath('//div[@class="c-article__content"]/*/text()').getall()
        content = response.selector.xpath('//div[@class="c-article__content"]')
        # 取得作者
        # 樓主
        floor = response.selector.xpath('//div[@class="c-post__header__author"]/a[1]/text()').getall()
        # 作者中文
        authorName = response.selector.xpath('//div[@class="c-post__header__author"]/a[2]/text()').getall()
        # 作者ID
        authorId = response.selector.xpath('//div[@class="c-post__header__author"]/a[3]/text()').getall()
        # 取得日期時間
        time = response.selector.xpath('//div[@class="c-post__header__info"]/*/text()').getall()
        print(title)

        # items['title'] = title
        items = []
        print(title)
        for index in range(len(authorId)):
            # print(str(index) + "-----------------------")
            # print(floor[index])
            # print(authorName[index])
            # print(authorId[index])
            # print(time[index])
            # print('message：' + content[index].xpath('string(.)').extract()[0])
            item = MyfirstscrapyprojectItem()

            contentData = content[index].xpath('string(.)').extract()[0]
            item['C10_NORMAL'] = pinyin(contentData, style=Style.NORMAL)
            item['C08_FIRST_LETTER'] = pinyin(contentData, style=Style.FIRST_LETTER)
            item['C09_INITIALS'] = pinyin(contentData, style=Style.INITIALS)
            item['C07_BOPOMOFO'] = pinyin(contentData, style=Style.BOPOMOFO)
            item['C06_BOPOMOFO_FIRST'] = pinyin(contentData, style=Style.BOPOMOFO_FIRST)
            item['C05_content'] = contentData
            item['C04_time'] = time[index]
            item['C03_floor'] = floor[index]
            item['C02_authorName'] = authorName[index]
            item['C01_authorId'] = authorId[index]
            item['C00_title'] = title
            yield item
            # items.append(item)

        # return items
        # 下一頁
        #
        next_page_url = response.xpath('//a[@class="next"]/@href').extract_first()
        url = response.urljoin(next_page_url)
        if url:
            yield scrapy.Request(url, callback=self.parseContent)


