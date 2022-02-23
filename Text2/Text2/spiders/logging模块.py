import scrapy
import logging

# 使用logger 进行输入`
logger = logging.getLogger(__name__)


class Logging模块Spider(scrapy.Spider):
    name = 'logging模块'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/']

    def parse(self, response):
        for i in range(10):
            item = {}
            item["name"] = "logging模块"
            # 方式一
            # logging.warning(item)
            # 2022-02-15 15:38:52 [root] WARNING: {'name': 'logging模块'}
            # 规定好的输出格式

            # 方式二：一般不使用第一种方式，输出完全看不到root目录
            logger.warning(item)
            # 方式三:传入pipeline
            yield item
