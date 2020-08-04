# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MyfirstscrapyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    C00_title = scrapy.Field()
    C03_floor = scrapy.Field()
    C02_authorName = scrapy.Field()
    C01_authorId = scrapy.Field()
    C04_time = scrapy.Field()
    C05_content = scrapy.Field()
    C10_NORMAL = scrapy.Field()
    C08_FIRST_LETTER = scrapy.Field()
    C09_INITIALS = scrapy.Field()
    C07_BOPOMOFO = scrapy.Field()
    C06_BOPOMOFO_FIRST = scrapy.Field()

