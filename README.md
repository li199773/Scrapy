# `Scrapy Learning`
****
## `1.简介`
### （1）Scrapy是用纯python实现的，一个为了爬取网站数据、提取结构性数据而编写的应用框架。
### （2）框架的力量，用户只需要定制开发几个模块就可以轻松的实现一个爬虫，用来抓取网页内容以及各种图片。
### （3）Scrapy使用了Twisted(其主要对手是Tornado)异步网络框架来处理网络通讯，可以加快我们的下载速度，不用自己去实现异步框架，并且包含了各种中间件接口，可以灵活的完成各种需求。
****
## `2.名称介绍`
### （1）Scrapy Engine(引擎)：负责Spider、ItemPipeline、DownLoader、Scheduler中间的通讯、信号、数据传递等。
### （2）Scheduler(调度器)：它负责接受Scrapy Engine发送过来的Request请求，并按照一定的方式进行整理排列，入队，当Scrapy Engine需要时，交还给Scrapy Engine。
### （3）Downloader(下载器)：负责下载Scrapy Engine发送的所有Requests请求，并将其获取到的Responses交还给Scrapy Engine，由Scrapy Engine交给Spider处理。
### （4）Spider(爬虫)：它负责处理所有Responses，从中分析提取数据，获取item字段需要的数据，并将需要跟进的URL提交给Scrapy Engine，再次进入Scheduler。
### （5）Item Pipeline(管道)：它负责处理Spider中获取到的Item,并进行后期处理(详细分析、过滤、存储等)。
### （6）Downloader Middlewares(下载中间件)：可以当做是一个可以自定义扩展下载功能的组件。
### （7）Spider Middlewares(Spider中间件)： 可以理解是一个可以自定扩展和操作Scrapider Engine和Spider中间通信的功能组件（比如进入Spider的Responses，和从Spider出去的Requests）
****
## `3、Scrapy的运作流程`
### （1）Scrapy Engine询问Spider要处理的网站，即爬取的域名范围，如`http://example.com`，同时也防止爬虫越界
### （2）Spider发送要处理的域名：`http://example.com`
### （3）Scrapy Engine会再次询问Spider要处理的第一个URL
### （4）Spider发送`http://example.com`给Scrapy Engine
### （5）Scrapy Engine会让Scheduler将requests请求排序入队
### （6）Scheduler处理requests
### （7）Scrapy Engine向Scheduler要处理好的requests请求
### （8）Scheduler发送处理好的requests给Scrapy Engine
### （9）Scrapy Engine要求Downloader按照Downloader Middlewares的设置下载requests请求
### （10）Downloader Middlewares将下载好的requests发送给Scrapy Engine。如果request下载失败，Scrapy Engine会告诉Scheduler，这个request下载失败了，需要记录一下，等会儿再下载。
### （11）Scrapy Engine返回给Spider下载好的requests，是一个responses对象，responses默认是交给Spider的def parse()这个函数处理的。
### （12）当Spider处理完responses后，如果有需要跟进的URL，会告诉Scrapy Engine，同时将处理好的Item数据提交给Scrapy Engine。
### （13）Scrapy Engine会将接收到的Item发送给Item Pipeline处理。同时将需要跟进的URL发送给Scheduler，让其循环处理，直到获取完需要的全部信息。
### （14）Item Pipeline处理获取到的Item。
#### 注意：只有当Scheduler中不存在任何request了，整个程序才会停止（如果requests中有下载失败的URL，Scrapy也会重新下载）。
****
# `Text1`
### `scrapy`创建
    scrapy startproject Text1
### `scrapy`启动
    scrapy crawl Tex1
****
## `主体介绍`
    name = 'demo'  # 爬虫名字
    allowed_domains = ['demo.cn']  # 允许爬虫的范围
    start_urls = ['https://demo.com']  # 最开始的url地址
### `settings.py`
    LOG_LEVEL = 'WARNING' # 消除警告，只保留输出主体部分
    
    # Configure item pipelines
    # See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
    ITEM_PIPELINES = {
    'Text1.pipelines.Text1Pipeline': 300,
    } #PIPELINES管道，实现item传输，300表示时间权重
### `items.py`
    # 将字典key先进行标注，防止使用错误
    name = scrapy.Field()
    name = scrapy.Field()
    name = scrapy.Field()
    name = scrapy.Field()
### `pipelines.py`
    # pipelines 管道 传递items
    class Text1Pipeline:
        def process_item(self, item, spider):
            item["style"] = "width"
            return item
    # 可同时定义多个class
    class Text1Pipeline1:
### `Text1/spider/xxx.py`
    item = {}
    # 使用xpath进行提取数据即可,得到的数据类型并不是一个列表类型
    yield item
    #yield返回传输给pipelines
****
# `Text2/spiders/logging模块`
    # 方式一
    # logging.warning(item)
    # 2022-02-15 15:38:52 [root] WARNING: {'name': 'logging模块'}
    # 规定好的输出格式
    # 方式二：一般不使用第一种方式，输出完全看不到root目录
    logger.warning(item)
    # 方式三:传入pipeline
    yield item
# `Text3/spider/tencent`
## `tencent.py`
    # start_requests这个函数首先进行运行
    def start_requests(self):
    # 使用字典推导式：cookies必须形成字典的形式
        cookies_dict = {cookie.split("=")[0]: cookie.split("=")[1] for cookie in cookies.split("; ")}
        # 传递给parse函数
        yield scrapy.Request(
            url=self.start_urls[0],
            callback=self.parse,
            cookies=cookies_dict
        )
## `pipelines.py`
    # 创建MySQL数据库进行存储
    keys = ', '.join(item.keys())
    values = ', '.join(['%s'] * len(item)) # 生成等量的 %S
    sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table="tencent", keys=keys, values=values)
****
# `Text4/spider/movie`
## `movie.py`
    # 重点是找到下一页的url
    next_url = response.xpath("//a[@class='next']/@href").extract_first()
    # 判断输出是否为None
    if next_url != None:
        yield scrapy.Request(next_url, callback=self.parse)
## `pipelines.py`
    import pymysql
    # 同理存入数据库
# `Text5/spider/sun0769`
## `sun0769.py`
    # 找到下一页然后将href传入到下一个函数中即可
    yield scrapy.Request(
                    item['href'],
                    callback=self.parse_detail,
                    meta={"item": item}
                )
## `pipelines.py`
    # 将数据库的连接放到open_spider中,这样只会进行一次连接操作
    def open_spider(self, spider):
         self.conn = pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="123456",
                database='scrapy_database',
            )
            self.cur = self.conn.cursor()
            self.cur.execute(sql)
**** 
# `Text6/spider/duanzi`
# `CrawlSpider`
## `duanzi.py`
    rules = (
        # LinkExtractor 链接提取器 提取url地址
        # callback 提取出来的url地址response会交给callback进行处理 可有可无
        # follow 当前url相应是能够重新进rule进行提取url地址
        Rule(LinkExtractor(allow=r'//www.xuexila.com/duanzi/jingdianduanzi/\d+\.html'), callback='parse_item'),  # .使用\进行转义,然后传给parse_item
        Rule(LinkExtractor(allow=r'/duanzi/jingdianduanzi/list_\d+\.html'), follow=True),  # 下一页不需要对页面进行处理
    )
****
# `Text7/spiders/tieba`
## `tieba.py`
# start_requests方法的重写
    def start_requests(self):
        cookies = ''
        # 使用字典推导式
        cookies_dict = {cookie.split("=")[0]: cookie.split("=")[1] for cookie in cookies.split("; ")}
        yield scrapy.Request(
            url=self.start_urls[0],
            callback=self.parse,
            cookies=cookies_dict
        )
