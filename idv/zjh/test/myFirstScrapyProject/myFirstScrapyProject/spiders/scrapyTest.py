import uuid
import time

import scrapy
from scrapy import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from idv.zjh.test.myFirstScrapyProject.myFirstScrapyProject.items import MyfirstscrapyprojectItem

titleDict = {}

class gammerSpider(scrapy.Spider):
    name = "bh3"
    allowes_domains = ["forum.gamer.com.tw"]
    # 崩壞三 討論列表
    start_urls = ('https://forum.gamer.com.tw/B.php?bsn=31066',)

    def __init__(self):
        executable_path = 'D:\\driver\\chromedriver.exe'
        self.driver = webdriver.chrome
        # 啟動無頭模式
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # 規避google bug
        chrome_options.add_argument('--disable-gpu')
        # driver = webdriver.Chrome(executable_path=executable_path,chrome_options=chrome_options)
        self.browser = webdriver.Chrome(executable_path=executable_path,chrome_options=chrome_options)
        # self.browser = webdriver.Chrome(executable_path=executable_path)
        # 設置等待時間
        # self.browser.implicitly_wait(30)

    # 進入留言網址
    def parse(self, response):
        # urls = response.css('a[class=b-list__main__title]').extract()
        # 單頁面測試
        next_page_url = response.xpath('//a[@class="b-list__main__title"]/@href').extract_first()
        url = response.urljoin(next_page_url)
        if url:
            yield scrapy.Request(url, callback=self.parseContent)
            # yield scrapy.Request(url, callback=self.parseContent)

        # 全部爬蟲
        # 進入文章內容
        # next_page_url = response.xpath('//a[@class="b-list__main__title"]/@href').extract()
        # for next in next_page_url:
        #     url = response.urljoin(next)
        #     # print(url)
        #     if url:
        #         yield scrapy.Request(url, callback=self.parseContent)
        #
        # next_page_url = response.xpath('//p[@class="b-list__main__title"]/@href').extract()
        # for next in next_page_url:
        #     url = response.urljoin(next)
        #     # print(url)
        #     if url:
        #         yield scrapy.Request(url, callback=self.parseContent)
        #
        # # 文章列表 下一頁
        # next_page_url = response.xpath('//a[@class="next"]/@href').extract_first()
        # url = response.urljoin(next_page_url)
        # if url:
        #     yield scrapy.Request(url, callback=self.parse)

    # 取得留言內容
    def parseContent(self, response):
        # 寫入檔案
        # print(response.body)
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        try:
            browser = self.browser
            # 設定URL
            browser.get(response.url)
            # 取得打開後的網址內容
            sel = Selector(text=browser.page_source)
            # 對所有留言點擊打開
            a_href = browser.find_elements_by_css_selector('a.more-reply')
            for a in a_href:
                browser.execute_script("arguments[0].click();", a)

            # 取得打開後的網址內容
            pageSource = browser.page_source
            sel = Selector(text=pageSource)
            # print(pageSource)
            # 取得現在時間
            spiderTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            # 取得頁面資訊
            # 標題
            title = sel.xpath('//h1[@class="title"]/text()').get()
            # 樓層
            floorDivs = sel.xpath('//div[@class="c-section__main c-post "]')

            # 設置 UUID 當文章主鍵
            titleUUID = uuid.uuid1()
            if title in titleDict:
                titleUUID = titleDict[title]
            else:
                titleUUID = uuid.uuid1()
                titleDict[title] = titleUUID

            #留言第一層
            for floorItem in floorDivs:
                floor = floorItem.xpath('.//div[@class="c-post__header__author"]/a[1]/text()').get()
                authorName = floorItem.xpath('.//div[@class="c-post__header__author"]/a[2]/text()').get()
                authorId = floorItem.xpath('.//div[@class="c-post__header__author"]/a[3]/text()').get()
                editTime = floorItem.xpath('.//div[@class="c-post__header__info"]/*/text()').get()[0:19]
                content = floorItem.xpath('.//div[@class="c-article__content"]').xpath('string(.)').extract()[0]
                item = MyfirstscrapyprojectItem()
                if floor == "樓主":
                    floor = 1
                    item['C00_title'] = title
                else:
                    print(floor)
                    floor = int(floor[:-2])

                item['C00_titleUUID'] = titleUUID
                item['C01_authorId'] = authorId
                item['C02_authorName'] = authorName
                item['C03_content'] = content
                item['C04_editTime'] = editTime
                item['C05_floor'] = floor
                item['C06_replyFloor'] = 0
                item['C99_spiderTime'] = spiderTime
                item['C99_URL'] = response.url



                # item['C06_BOPOMOFO_FIRST'] = pinyin(contentData, style=Style.BOPOMOFO_FIRST)
                # item['C07_BOPOMOFO'] = pinyin(contentData, style=Style.BOPOMOFO)
                # item['C08_FIRST_LETTER'] = pinyin(contentData, style=Style.FIRST_LETTER)
                # item['C09_INITIALS'] = pinyin(contentData, style=Style.INITIALS)
                # item['C10_NORMAL'] = pinyin(contentData, style=Style.NORMAL)
                yield item

            # 第二層留言
            for replyDivs in floorDivs:
                replyDiv = replyDivs.xpath('.//div[@class="c-reply__item"]')
                if len(replyDiv) != 0:
                    floor = replyDivs.xpath('.//div[@class="c-post__header__author"]/a[1]/text()').get()
                    if floor == "樓主":
                        floor = 1
                    else:
                        print(floor)
                        floor = int(floor[:-2])
                    replyFloor = 0
                    for replyItem in replyDiv:
                        replyFloor = replyFloor + 1
                        authorId = replyItem.xpath('.//a[@class="reply-content__user"]/@href').get()[20:]
                        authorName = replyItem.xpath('.//a[@class="reply-content__user"]/text()').get()
                        content = replyItem.xpath('.//article[@class="reply-content__article c-article "]').xpath('string(.)').extract()[0]
                        editTime = replyItem.xpath('.//div[@class="edittime"]/text()').get()[0:19]
                        item = MyfirstscrapyprojectItem()
                        item['C00_titleUUID'] = titleUUID
                        item['C01_authorId'] = authorId
                        item['C02_authorName'] = authorName
                        item['C03_content'] = content
                        item['C04_editTime'] = editTime
                        item['C05_floor'] = floor
                        item['C06_replyFloor'] = replyFloor
                        item['C99_spiderTime'] = spiderTime
                        item['C99_URL'] = response.url

                        yield item

        except Exception as e:
            print("發生錯誤：" + e)

        # 下一頁
        #
        next_page_url = response.xpath('//a[@class="next"]/@href').extract_first()
        url = response.urljoin(next_page_url)
        if url:
            yield scrapy.Request(url, callback=self.parseContent)