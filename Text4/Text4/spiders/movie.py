import scrapy


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['1905.com']
    start_urls = ['https://www.1905.com/vod/list/n_1/o3p2.html']

    def parse(self, response):
        item = {}
        rets = response.xpath("//section[@class='mod row search-list']/div")
        for ret in rets:
            item["movie_name"] = ret.xpath(".//a/h3/text()").extract_first()
            item["brief_introduction"] = ret.xpath(".//a/p/text()").extract_first()
            score_integer = ret.xpath(".//i/b/text()").extract_first()
            score_decimal = ret.xpath(".//a/i/text()").extract_first()
            item["score"] = "{}{}".format(score_integer, score_decimal)
            # 去除None值
            if item["movie_name"] != None:
                yield item
        # 找到下一页的url
        next_url = response.xpath("//a[@class='next']/@href").extract_first()
        # 判断输出是否为None
        if next_url != None:
            yield scrapy.Request(next_url, callback=self.parse)
