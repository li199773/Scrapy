import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DuanziSpider(CrawlSpider):
    name = 'duanzi'
    allowed_domains = ['xuexila.com']
    start_urls = ['https://www.xuexila.com/duanzi/jingdianduanzi/list_1.html']
    # 提取url规则的定义，是一个元祖，有顺序的限制
    rules = (
        # LinkExtractor 链接提取器 提取url地址
        # callback 提取出来的url地址response会交给callback进行处理 可有可无
        # follow 当前url相应是能够重新进rule进行提取url地址
        Rule(LinkExtractor(allow=r'//www.xuexila.com/duanzi/jingdianduanzi/\d+\.html'), callback='parse_item'),  # .使用\进行转义
        Rule(LinkExtractor(allow=r'/duanzi/jingdianduanzi/list_\d+\.html'), follow=True),  # 下一页不需要对页面进行处理
    )

    def parse_item(self, response):
        item = {}

        item["title"] = response.xpath("//div[@class='ar_title']//h1/text()").extract_first()
        item["date"] = response.xpath("//div[@class='sub_title clear']//span[1]//time[@class='fxtime']/text()").extract_first()
        # item["content"] = response.xpath("//div[@class='con_article con_main']//p[1]/text()").extract_first()
        if item["date"] != None:
            print(item)
