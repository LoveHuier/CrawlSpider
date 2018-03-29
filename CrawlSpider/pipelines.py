# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json


class CrawlspiderPipeline(object):
    def __init__(self):
        self.file = codecs.open("/home/mata/dataex/news_data.json", "wb", encoding='utf-8')

    def process_item(self, item, spider):
        # i = json.dumps(dict(item), ensure_ascii=False)
        # line = i + '\n'
        for j in range(0, len(item['name'])):
            name = item['name'][j]
            link = item['link'][j]

            news = {"name": name, "link": link}
            i = json.dumps(news, ensure_ascii=False)
            line = i + '\n'
            self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()
