from datetime import datetime

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class CheckItemPipeline:
    def process_item(self, article, spider):
        if not article['title'] \
            or not article['url'] \
                or not article['lastUpdated']:
            raise DropItem('Missing something!')
        return article


class CleanDatePipeline:
    def process_item(self, article, spider):
        article['lastUpdated'].replace('This page was last edited on', '').strip()
        article['lastUpdate'] = datetime.strptime(article['lastUpdated'], '%d %B %Y, at %H:%M')
