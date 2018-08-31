# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookSpider(CrawlSpider):
    name = 'book'
    allowed_domains = ['www.amazon.cn','www.amazon.cn']
    start_urls = ['https://www.amazon.cn/图书/b?node=658390051']

    rules = (
        Rule(LinkExtractor(allow=r'/s/ref=lp_'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        a_list = response.xpath('//div[@class="ch-tabwidget-asintitle"]/a/text()').extract()
        print(a_list)

        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
