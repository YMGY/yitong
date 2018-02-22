# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from settings import MONGODB


class IcisbenPipeline(object):
    collection_name = 'ccfPrice'
    db_name = 'ccf'

    def process_item(self, item, spider):
        oldItem = self.db[self.collection_name].find_one({'Name': item['Name'], 'ReportDate': item['ReportDate']})
        if not oldItem:
            self.db[self.collection_name].insert_one(dict(item))
        return item

    def __init__(self):
        self.host = MONGODB.get('host')
        self.port = MONGODB.get('port')

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host=self.host, port=self.port)
        self.db = self.client[self.db_name]

    def close_spider(self, spider):
        self.client.close()
