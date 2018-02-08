# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IcisMegItem(scrapy.Item):
    DisplaySeriesId = scrapy.Field()
    ReportDate = scrapy.Field()
    StandardReportDate = scrapy.Field()
    CommodityName = scrapy.Field()
    LocationName = scrapy.Field()
    UnitDisplay = scrapy.Field()
    PriceDeltaLow = scrapy.Field()
    PriceDeltaValueLow = scrapy.Field()
    PriceLow = scrapy.Field()
    PriceDeltaHigh = scrapy.Field()
    PriceDeltaValueHigh = scrapy.Field()
    PriceHigh = scrapy.Field()
    PriceDeltaMid = scrapy.Field()
    PriceDeltaValueMid = scrapy.Field()
    PriceMid = scrapy.Field()
    Volatility = scrapy.Field()
    Volume = scrapy.Field()
    NumberOfTrades = scrapy.Field()
    IsEnergy = scrapy.Field()
    Name = scrapy.Field()
    DeliveryPeriod = scrapy.Field()
    TradeTypes = scrapy.Field()
    DomainTypeFlagValue = scrapy.Field()
    TransportName = scrapy.Field()
    QuotationComments = scrapy.Field()
