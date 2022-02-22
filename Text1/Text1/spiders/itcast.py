import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'  # 爬虫名字
    allowed_domains = ['itcast.cn']  # 允许爬虫的范围
    start_urls = ['https://sc.chinaz.com/tupian/']  # 最开始的url地址

    # 紧接着进入下面的程序
    def parse(self, response):
        item = {}
        # 开始处理start_urls的地址
        # 使用xpath进行提取数据即可,得到的数据类型并不是一个列表类型
        ret = response.xpath("//div[@id='container']/div")  # .extract 提取data
        for li in ret:
            item["name"] = li.xpath(".//div//a//img/@alt").extract_first()
            item["href"] = li.xpath(".//div//a//@href").extract_first()
            yield item
