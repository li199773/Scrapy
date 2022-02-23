# -*- coding: utf-8 -*-
# @Time : 2022/2/15 16:30
# @Author : O·N·E
# @File : logging_learning.py
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                    datefmt='%a %d %b %Y %H:%M:%S',
                    filemode='w')

logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logger.info("this is logging")
