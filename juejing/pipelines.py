# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import time
import pymongo

DATABASE_IP = '127.0.0.1'
DATABASE_PORT = 27017
DATABASE_NAME = 'sun'
client = pymongo.MongoClient(DATABASE_IP, DATABASE_PORT)
db = client.sun
# db.authenticate("dba", "dba")
collection = db.jujin  # 准备插入数据

class JuejingPipeline(object):
    def process_item(self, item, spider):
        try:
            collection.insert(item)
        except Exception as e:
            print(e.args)
