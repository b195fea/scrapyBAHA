# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MyfirstscrapyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    floor = scrapy.Field()
    authorName = scrapy.Field()
    authorId = scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()