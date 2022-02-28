# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Text3Item(scrapy.Item):
    # define the fields for your item here like:
    RecruitPostName = scrapy.Field()
    CategoryName = scrapy.Field()
    CountryName = scrapy.Field()
    LocationName = scrapy.Field()
    PostURL = scrapy.Field()
    LastUpdateTime = scrapy.Field()

