import uuid
import time

import scrapy
from scrapy import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from idv.zjh.scrapy.gammer.news.news.items import NewsItem
from scrapy import cmdline

if __name__ == '__main__':
    cmdline.execute("scrapy crawl news".split())


class gammerSpider(scrapy.Spider):
    name = "news"

    allowes_domains = ["m.gamer.com.tw"]
    # 巴哈姆特 討論列表
    start_urls = ('https://m.gamer.com.tw/index.php?page=1&t=GNN&k=0',)

    def __init__(self):
        executable_path = 'D:\\driver\\chromedriver89.exe'
        self.driver = webdriver.chrome
        # 啟動無頭模式
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # 規避google bug
        chrome_options.add_argument('--disable-gpu')
        # driver = webdriver.Chrome(executable_path=executable_path,chrome_options=chrome_options)
        self.browser = webdriver.Chrome(executable_path=executable_path,chrome_options=chrome_options)
        # 設置等待時間
        # self.browser.implicitly_wait(30)

    # 進入留言網址
    def parse(self, response):
        # 取得當前頁碼
        pagenow = response.xpath('//a[@class="pagenow"]/text()').get()
        if pagenow != None:
            # 內文
            next_page_content_url = response.xpath('//section[@class="index-boxC"]/a/@href').extract()
            for next in next_page_content_url:
                url = response.urljoin(next)
                if url:
                    yield scrapy.Request(url, callback=self.parseContent)

            # 文章列表 下一頁
            pagenow = int(pagenow) + 1
            # 下一個列表畫面
            next_page_url = 'https://m.gamer.com.tw/index.php?page={}&t=GNN&k=0'.format(pagenow)
            url = response.urljoin(next_page_url)
            if url:
                yield scrapy.Request(url, callback=self.parse)

    # 取得留言內容
    def parseContent(self, response):
        # 設定URL
        try:
            browser = self.browser
            # 設定URL
            browser.get(response.url)
            # 取得打開後的網址內容
            sel = Selector(text=browser.page_source)
            # 對所有留言點擊打開
            sel = Selector(text=browser.page_source)
            # node1 = sel.xpath('//meta[@property="og:title"]/@content')
            # print(node1.extract_first())
            title = sel.xpath('//meta[@property="og:title"]/@content').extract_first()
            content = sel.xpath('//article[@class="gnn_box"]').xpath('string(..)').extract_first()
            item = NewsItem()
            item['C00_title'] = title
            item['C03_content'] = content
            item['C99_URL'] = response.url
            yield item
        except Exception as e:
            print("發生錯誤：" + e)