# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CcfItem(scrapy.Item):
    name = scrapy.Field()
    market = scrapy.Field()
    publishDate = scrapy.Field()
    price = scrapy.Field()
    unit = scrapy.Field()
