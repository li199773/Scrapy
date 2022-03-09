# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Text5Item(scrapy.Item):
    # define the fields for your item here like:
    state = scrapy.Field()
    title = scrapy.Field()
    href = scrapy.Field()
    update_time = scrapy.Field()
    content_img = scrapy.Field()
    content_text = scrapy.Field()
    pass
