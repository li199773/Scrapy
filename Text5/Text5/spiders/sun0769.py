import scrapy
from Text5.items import Text5Item


class Sun0769Spider(scrapy.Spider):
    name = 'sun0769'
    allowed_domains = ['sun0769.com']
    start_urls = ['https://wz.sun0769.com/political/index/politicsNewest?id=1&page=1']

    def parse(self, response):
        tr_list = response.xpath("//div[@class='width-12']//ul[2]/li")
        for tr in tr_list:
            item = Text5Item()
            item["state"] = str(tr.xpath(".//span[2]/text()").extract_first()).strip()
            item["title"] = tr.xpath(".//span[3]/a/text()").extract_first()
            item["href"] = "https://wz.sun0769.com" + tr.xpath(".//span[3]/a/@href").extract_first()
            item["update_time"] = tr.xpath(".//span[5]/text()").extract_first()
            yield scrapy.Request(
                item['href'],
                callback=self.parse_detail,
                meta={"item": item}
            )

    def parse_detail(self, response):
        item = response.meta["item"]
        item["content_img"] = response.xpath("//div[@class='clear details-img-list Picture-img']/img/@src").extract_first()
        item["content_text"] = response.xpath("//div[@class='details-box']/pre/text()").extract_first()
        yield item
