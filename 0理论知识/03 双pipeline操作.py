# -*- coding: utf-8 -*-
# @Time : 2022/2/15 14:34
# @Author : O·N·E
# @File : 03 双pipeline操作.py
"""
class Text1Pipeline:
    def process_item(self, item, spider):
        item["style"] = "width"
        return item


class Text1Pipeline1:
    def process_item(self, item, spider):
        print(item)
        return item

# 首先进入Text1Pipeline，然后在进入Text1Pipeline1 输出检测得以证明双Pipeline
"""
