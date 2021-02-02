# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


# class MyfirstscrapyprojectPipeline:
#     def process_item(self, item, spider):
#         return item

class MongoDBPipeline:
    def open_spider(self, spider):
        db_uri = spider.settings.get('MONGODB_URI', 'mongodb://localhost:27017')
        db_name = spider.settings.get('MONGODB_DB_NAME', 'scrapy')
        self.db_client = MongoClient('mongodb://localhost:27017')
        self.db = self.db_client[db_name]

    def process_item(self, item, spider):
        self.insert_bh3(item)
        return item

    def insert_bh3(self, item):
        try:
            item = dict(item)
            self.db.bh3_content.insert_one(item)
        except Exception as e:
            print(e)

    def close_spider(self, spider):
        try:
            self.db_client.close()
        except Exception as e:
            print(e)

