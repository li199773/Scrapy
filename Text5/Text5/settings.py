# Scrapy settings for Text5 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Text5'

SPIDER_MODULES = ['Text5.spiders']
NEWSPIDER_MODULE = 'Text5.spiders'
LOG_LEVEL = 'WARNING'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'BIDUPSID=06A17A73F8F44DEC3E44B1EC84FD6302; PSTM=1627654483; __yjs_duid=1_7a84e79fa43f16459243d02e1d7e8b5c1627825360188; bdshare_firstime=1629703094461; H_WISE_SIDS=107317_110085_127969_179347_181126_181588_182246_182273_182530_183031_183328_184010_184441_185268_185635_185650_186317_186716_186840_186896_187346_187433_187819_187877_188182_188452_188844_188873_188997_189091_189422_189679_189715_189732_189755_190034_190114_190152_190474_190510_190680_190681_190756_190779_190804_190863_191051_191244_191359_191419_191475_191503_191598_191640_191809_192132_192264_192275_192408_192875_192905_192957_193010_193043_193179_193194_193283_193320_193492_193516_193701_193755_194122_194519_194670; BAIDUID=DEE38E821D1227538434B7B2EA6841DB:FG=1; MCITY=-131%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; st_key_id=17; USER_JUMP=-1; video_bubble0=1; delPer=0; PSINO=2; ariaDefaultTheme=default; BAIDU_WISE_UID=wapp_1645426488214_567; ariaFixed=true; wise_device=0; Hm_lvt_287705c8d9e2073d13275b18dbd746dc=1645426580; ariaReadtype=1; ariaoldFixedStatus=false; ariaStatus=false; BAIDUID_BFESS=025D8EC593C9A75C8A0C6362CA800D33:FG=1; tb_as_data=95b40d3a84d10b7bb08f974c85cd53b2b42e8c730ea563b9774287b01b4e2cd94c283762a6500f642b72f6578480335e6e9d09cae5a78a941831fd2df928e935e93f7dc5a81b1f8410d8136abd00941664063ac4bf796672fcb0ede335c34cca; Hm_lpvt_287705c8d9e2073d13275b18dbd746dc=1645496090; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1645494055,1645495420,1645496091,1645511836; H_PS_PSSID=35104_35762_34584_35491_35872_35245_35956_35319_26350_35942; BCLID=10839602634511238264; BDSFRCVID=sx8OJeC62AZEtibDQ037tWM5iDq4m7nTH6aonawhd_qNiE5Gh_iYEG0Phx8g0Ku-S2MAogKK0mOTHv8F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tJ4OoIK-tDK3DbTG2boqqRkObmT22jnvKGR9aJ5nJD_MjbvoDp5ULxCVjqOUW6Q05m3BWlFbQpP-HJAw0IcUW4IpW2ceaJQbJT5XKl0MLp6Wbb0xynoD5KuubxnMBMPjamOnaPLy3fAKftnOM46JehL3346-35543bRTLnLy5KJtMDF4D5A2jjjXjHRQaRQObCIXXnbDHJO_bUbXyfnkbfJBDGO3aMPeLenG2qCXbU3YMJTNyP6Vy6t7yajK25cgHmnzBqc9H4O8fJ-m2tTpQT8rXqAOK5OibCrJsxjDab3vOIJzXpO156kzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksDMDtqjtJfnFj_CKXfb3hHJrFMtL_KJoH-UnLqh8HX2OZ0l8KtJRSDMoI-xOdeqLj5bJut4c-WK6p-bcmWIQHDUOLMlD23qku5hjMbML80Cn4KKJxJRLWeIJo5fc4KRLPhUJiB5OLBan7LDnIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbC8RD58hejj0eUrJeJjtaDr3Q5r2a-t3b56oXU6qLT5X2-bR-jKq3gJfaxQ2QhChjtbkqJJ23h0njxQyhjvpBIJKQlbw-UjTElrC0xonDh8UXH7MJUntKHrRW4OO5hvvhb6O3M7-eMKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQbG_EJ6tOtRIH_Kv55RrOfjrP-trf5DCShUFsbbkOB2Q-5KL-0xcpfbTPQhL2DT-33PFtax3DJIDfWfbdJJjoDRj6M-OrKfCtQHoxapR0ymTxoUJSMInJhhvGqq-KXf_ebPRiJPr9QgbqVpQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0M5DK0HPonHjLbD5Jy3f; BCLID_BFESS=10839602634511238264; BDSFRCVID_BFESS=sx8OJeC62AZEtibDQ037tWM5iDq4m7nTH6aonawhd_qNiE5Gh_iYEG0Phx8g0Ku-S2MAogKK0mOTHv8F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tJ4OoIK-tDK3DbTG2boqqRkObmT22jnvKGR9aJ5nJD_MjbvoDp5ULxCVjqOUW6Q05m3BWlFbQpP-HJAw0IcUW4IpW2ceaJQbJT5XKl0MLp6Wbb0xynoD5KuubxnMBMPjamOnaPLy3fAKftnOM46JehL3346-35543bRTLnLy5KJtMDF4D5A2jjjXjHRQaRQObCIXXnbDHJO_bUbXyfnkbfJBDGO3aMPeLenG2qCXbU3YMJTNyP6Vy6t7yajK25cgHmnzBqc9H4O8fJ-m2tTpQT8rXqAOK5OibCrJsxjDab3vOIJzXpO156kzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksDMDtqjtJfnFj_CKXfb3hHJrFMtL_KJoH-UnLqh8HX2OZ0l8KtJRSDMoI-xOdeqLj5bJut4c-WK6p-bcmWIQHDUOLMlD23qku5hjMbML80Cn4KKJxJRLWeIJo5fc4KRLPhUJiB5OLBan7LDnIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbC8RD58hejj0eUrJeJjtaDr3Q5r2a-t3b56oXU6qLT5X2-bR-jKq3gJfaxQ2QhChjtbkqJJ23h0njxQyhjvpBIJKQlbw-UjTElrC0xonDh8UXH7MJUntKHrRW4OO5hvvhb6O3M7-eMKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQbG_EJ6tOtRIH_Kv55RrOfjrP-trf5DCShUFsbbkOB2Q-5KL-0xcpfbTPQhL2DT-33PFtax3DJIDfWfbdJJjoDRj6M-OrKfCtQHoxapR0ymTxoUJSMInJhhvGqq-KXf_ebPRiJPr9QgbqVpQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0M5DK0HPonHjLbD5Jy3f; SEARCH_MARKET_URL=https%253A//wenku.baidu.com/tfview/2342b63ece7931b765ce0508763231126edb773b.html%253Ffr%253Dlaunch_ad%2526SS-bdtg01%2526utm_source%253Dbdss-WD%2526utm_medium%253Dcpc%2526utm_account%253DSS-bdtg01%2526e_creative%253D54642329588%2526e_keywordid%253D342405088199%2526bd_vid%253D10839602634511238264; BA_HECTOR=042k05ah2kah242kmg1h192fv0r; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1645514033; ab_sr=1.0.1_ZDkxOTA3Nzk1ZDMwYjQ3MDFlNDU5MjU3MTA0NTYzOTg2MjljZTY0MzEwY2YwMmJmYzc5ODVkOWFmZmRiZjg5MzNkZDQxY2VjZmU0ZWNhZjgxNDQyM2Q1OTQwNGI5NTNkZThmNzdjOWNmMDk2YjAwY2QyNmI5MDhiNWQyYjE2MDI1ZjFlNzc3Y2FlNGIzMWI2NjNiODk1OGJmYWQwNzNiMg==; st_data=1bfc59fe3bcc810224228c458e5fd922e081727c907635cd04f15082bc2c4d1ff8fe40a686813bbf49f7e9a6d93cbc748ded226c2558c852cc90790170bd38e4a61a64240fcfa0bafa9ef19f47c370b5981af51cacacfe0cb16de67673b8dbba; st_sign=a4e35fe8',
    'Host': 'tieba.baidu.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'Text5.middlewares.Text5SpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'Text5.middlewares.Text5DownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'Text5.pipelines.Text5Pipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
