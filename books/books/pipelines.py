# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class BooksPipeline:
    
    collection_name = "books_monteillet"
    
    def open_spider(self, spider):
        self.client = MongoClient("mongodb+srv://christoloisel:Rose230323@cluster0.soahdz4.mongodb.net/")
        self.db = self.client["books_monteillet"]
        
    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(ItemAdapter(item).asdict())
        return item

    def close_spider(self, spider):
        self.client.close()