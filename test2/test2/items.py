# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class sku(scrapy.Item):
    # define the fields for your item here like:
    # url= scrapy.Field()
    name = scrapy.Field()
    avail = scrapy.Field()
    price = scrapy.Field()
    packSize= scrapy.Field()

class sku2(scrapy.Item):
    # define the fields for your item here like:
    # url= scrapy.Field()
    name = scrapy.Field()
    avail = scrapy.Field()
    price = scrapy.Field()
    packSize= scrapy.Field()
    variants=scrapy.Field()

    
