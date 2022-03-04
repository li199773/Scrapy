# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Text4Item(scrapy.Item):
    # define the fields for your item here like:
    movie_name = scrapy.Field()
    brief_introduction = scrapy.Field()
    score = scrapy.Field()
    pass
