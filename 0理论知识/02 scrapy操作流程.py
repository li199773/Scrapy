# -*- coding: utf-8 -*-
# @Time : 2022/2/14 15:52
# @Author : O·N·E
# @File : 02 scrapy操作流程.py
"""
1.安装scrapy：
    pip install scrapy -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
2.创建scrapy项目：
    scrapy startproject Text1
3.设定处理网站的域名范围，防止越界
    scrapy genspider itcast itcast.cn
4.settings
    #LOG_LEVEL = 'WARNING' # 设置等级 取消日志的输出
5.pipelines存储
    # 开启
    ITEM_PIPELINES = {
    'Text1.pipelines.Text1Pipeline': 300,
    使用yield进行传输，减少内存的占有
}
"""
