# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Film_Name = scrapy.Field()  # Define objects to automatically generate pairs of dictionary pairs of keys,values.
    Film_Date = scrapy.Field()
    Film_Country = scrapy.Field()
    Film_Rate = scrapy.Field()
    Director = scrapy.Field()
    Stars = scrapy.Field()