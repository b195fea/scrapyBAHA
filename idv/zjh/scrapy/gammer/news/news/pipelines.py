# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

class NewsPipeline:
    def open_spider(self, spider):
        db_uri = spider.settings.get('MONGODB_URI')
        db_name = spider.settings.get('MONGODB_DB_NAME')
        self.db_client = MongoClient(db_uri)
        self.db = self.db_client[db_name]

    def process_item(self, item, spider):
        self.insert(item)
        return item

    def insert(self, item):
        try:
            item = dict(item)
            self.db.scrapy_news.insert_one(item)
        except Exception as e:
            print(e)

    def close_spider(self, spider):
        try:
            self.db_client.close()
        except Exception as e:
            print(e)

