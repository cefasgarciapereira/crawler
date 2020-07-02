# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AgencialupacrawlerItem(scrapy.Item):
    link = scrapy.Field()
    pass

class LupaNewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    time = scrapy.Field()
    link = scrapy.Field()
    body = scrapy.Field()
    label = scrapy.Field()
    pass
