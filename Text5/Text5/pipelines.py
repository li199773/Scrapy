# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re
import pymysql


class Text5Pipeline:
    def open_spider(self, spider):
        sql = "create table if not exists sun0769 " + """(
                                        `content_img` varchar(255) DEFAULT NULL,
                                        `content_text` varchar(8000) DEFAULT NULL,
                                        `href` varchar(255) DEFAULT NULL,
                                        `state` varchar(255) DEFAULT NULL,
                                        `title` varchar(255) DEFAULT NULL,
                                        `update_time` varchar(255) DEFAULT NULL
                                        )
                                    """

        self.conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="123456",
            database='scrapy_database',
        )
        self.cur = self.conn.cursor()
        self.cur.execute(sql)
        print("database create ok")

    def process_item(self, item, spider):
        item["content_text"] = self.process_content_text(item["content_text"])
        keys = ', '.join(item.keys())
        values = ', '.join(['%s'] * len(item))
        try:
            sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table="sun0769", keys=keys, values=values)
            # 将字段的value转化为元祖存入
            self.cur.execute(sql, tuple(item.values()))
            self.conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
        return item

    def process_content_text(self, content_text):
        content_text = re.sub(r"\r\n", "", content_text)
        if len(content_text) > 0:
            return content_text
