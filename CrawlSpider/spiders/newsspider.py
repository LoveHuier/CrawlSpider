# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from CrawlSpider.items import CrawlspiderItem


class NewsspiderSpider(CrawlSpider):
    name = 'newsspider'
    allowed_domains = ['sohu.com']
    start_urls = ('http://news.sohu.com/',)

    rules = (
        Rule(LinkExtractor(allow='http://www.sohu.com/a/\d{9}_\d{6}'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = CrawlspiderItem()
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        item['name'] = response.xpath('//a[@target="_blank"]/text()').extract()
        item['link'] = response.xpath('//a[@target="_blank"]/@href').extract()
        return item
