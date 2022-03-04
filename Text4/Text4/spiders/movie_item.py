import scrapy
from Text4.items import Text4Item


class MovieItemSpider(scrapy.Spider):
    name = 'movie_item'
    allowed_domains = ['1905.com']
    start_urls = ['https://www.1905.com/vod/list/n_1/o3p1.html']

    def parse(self, response):
        item = Text4Item()
        rets = response.xpath("//section[@class='mod row search-list']/div")
        for ret in rets:
            item["movie_name"] = ret.xpath(".//a/h3/text()").extract_first()
            item["brief_introduction"] = ret.xpath(".//a/p/text()").extract_first()
            score_integer = ret.xpath(".//i/b/text()").extract_first()
            score_decimal = ret.xpath(".//a/i/text()").extract_first()
            item["score"] = "{}{}".format(score_integer, score_decimal)
            if item["movie_name"] != None:
                yield item
