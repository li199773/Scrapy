# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

sql = "create table if not exists tencent " + """(
                                `RecruitPostName` varchar(255) DEFAULT NULL,
                                `CategoryName` varchar(255) DEFAULT NULL,
                                `CountryName` varchar(255) DEFAULT NULL,
                                `LocationName` varchar(255) DEFAULT NULL,
                                `PostURL` varchar(255) DEFAULT NULL,
                                `LastUpdateTime` varchar(255) DEFAULT NULL
                                )
                            """

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    database='scrapy_database',
)
cur = conn.cursor()
cur.execute(sql)
print("ok")


class Text3Pipeline:
    def process_item(self, item, spider):
        # print(item)
        keys = ', '.join(item.keys())
        values = ', '.join(['%s'] * len(item))
        try:
            sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table="tencent", keys=keys, values=values)
            # 将字段的value转化为元祖存入
            cur.execute(sql, tuple(item.values()))
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()

        return item
