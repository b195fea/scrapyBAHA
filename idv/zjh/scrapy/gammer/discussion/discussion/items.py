# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DiscussionItem(scrapy.Item):
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
    # C10_NORMAL = scrapy.Field()
    # C08_FIRST_LETTER = scrapy.Field()
    # C09_INITIALS = scrapy.Field()
    # C07_BOPOMOFO = scrapy.Field()
    # C06_BOPOMOFO_FIRST = scrapy.Field()

