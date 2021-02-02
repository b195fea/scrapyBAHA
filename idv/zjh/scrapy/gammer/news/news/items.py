# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    # define the fields for your item here like:
    C00_titleUUID = scrapy.Field()
    C00_title = scrapy.Field()
    C01_authorId = scrapy.Field()
    C02_authorName = scrapy.Field()
    C03_content = scrapy.Field()
    C04_editTime = scrapy.Field()
    C05_floor = scrapy.Field()
    C06_replyFloor = scrapy.Field()
    C99_spiderTime = scrapy.Field()
    C99_URL = scrapy.Field()
