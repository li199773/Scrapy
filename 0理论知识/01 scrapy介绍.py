# -*- coding: utf-8 -*-
# @Time : 2022/2/14 15:47
# @Author : O·N·E
# @File : 01 scrapy介绍.py
"""
1.简介
    （1）Scrapy是用纯python实现的，一个为了爬取网站数据、提取结构性数据而编写的应用框架。
    （2）框架的力量，用户只需要定制开发几个模块就可以轻松的实现一个爬虫，用来抓取网页内容以及各种图片。
    （3）Scrapy使用了Twisted(其主要对手是Tornado)异步网络框架来处理网络通讯，可以加快我们的下载速度，不用自己取实现异步框架，并且包含了各种中间件接口，可以灵活的完成各种需求。
2.名称介绍
    （1）Scrapy Engine(引擎)：负责Spider、ItemPipeline、DownLoader、Scheduler中间的通讯、信号、数据传递等。
    （2）Scheduler(调度器)：它负责接受Scrapy Engine发送过来的Request请求，并按照一定的方式进行整理排列，入队，当Scrapy Engine需要时，交还给Scrapy Engine。
    （3）Downloader(下载器)：负责下载Scrapy Engine发送的所有Requests请求，并将其获取到的Responses交还给Scrapy Engine，由Scrapy Engine交给Spider处理。
    （4）Spider(爬虫)：它负责处理所有Responses，从中分析提取数据，获取item字段需要的数据，并将需要跟进的URL提交给Scrapy Engine，再次进入Scheduler。
    （5）Item Pipeline(管道)：它负责处理Spider中获取到的Item,并进行后期处理(详细分析、过滤、存储等)。
    （6）Downloader Middlewares(下载中间件)：可以当做是一个可以自定义扩展下载功能的组件。
    （7）Spider Middlewares(Spider中间件)： 可以理解是一个可以自定扩展和操作Scrapider Engine和Spider中间通信的功能组件（比如进入Spider的Responses，和从Spider出去的Requests）
3、Scrapy的运作流程
　　（1）Scrapy Engine询问Spider要处理的网站，即爬取的域名范围，如http://example.com，这同时也防止爬虫越界
　　（2）Spider发送要处理的域名：`http://example.com`
　　（3）Scrapy Engine会再次询问Spider要处理的第一个URL
　　（4）Spider发送`http://xxxxxx.com`给Scrapy Engine
　　（5）Scrapy Engine会让Scheduler将requests请求排序入队
　　（6）Scheduler处理requests
　　（7）Scrapy Engine向Scheduler要处理好的requests请求
　　（8）Scheduler发送处理好的requests给Scrapy Engine
　　（9）Scrapy Engine要求Downloader按照Downloader Middlewares的设置下载requests请求
　　（10）Downloader Middlewares将下载好的requests发送给Scrapy Engine。如果request下载失败，Scrapy Engine会告诉Scheduler，这个request下载失败了，需要记录一下，等会儿再下载。
　　（11）Scrapy Engine返回给Spider下载好的requests，是一个responses对象，responses默认是交给Spider的def parse()这个函数处理的。
　　（12）当Spider处理完responses后，如果有需要跟进的URL，会告诉Scrapy Engine，同时将处理好的Item数据提交给Scrapy Engine。
　　（13）Scrapy Engine会将接收到的Item发送给Item Pipeline处理。同时将需要跟进的URL发送给Scheduler，让其循环处理，直到获取完需要的全部信息。
　　（14）Item Pipeline处理获取到的Item。
　　注意：只有当Scheduler中不存在任何request了，整个程序才会停止（如果requests中有下载失败的URL，Scrapy也会重新下载）。
"""
