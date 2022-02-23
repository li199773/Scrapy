# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging

logger = logging.getLogger(__name__)


class Text2Pipeline:
    def process_item(self, item, spider):
        logger.warning("--" * 20)
        return item
