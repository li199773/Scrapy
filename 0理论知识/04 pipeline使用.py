# -*- coding: utf-8 -*-
# @Time : 2022/2/15 15:06
# @Author : O·N·E
# @File : 04 pipeline使用.py
"""
使用pipeline
    从pipeline的字典形式可以看出，pipeline可以由多个，pipeline也可以定义多个，为什么要定义多个pipeline？
    1.可能会有多个spider，不用的pipelinepipeline处理不用的item内容
    2.一个spider的内容可能要做不用的操作，比如存入不同的数据库中
说明：
    1.pipeline的权重越小优先级越高
    2.pipeline中的process_item方法名不能修改为其他的名称
open_spider(self,spider)：使用
    在爬虫开始时候进行执行，只执行一次
    常用在数据库的链接，只需要链接一次即可
close_spider(self,spider)：使用
    在爬虫关闭时候进行执行，只执行一次
"""
