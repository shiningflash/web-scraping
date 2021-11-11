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
        lastUpdated = article['lastUpdated'].split('on')[1].strip()
        article['lastUpdated'] = datetime.strptime(lastUpdated, '%d %B %Y, at %H:%M')
        return article


class NewsScraperPipeline:
    def process_item(self, item, spider):
        # item['date'] = datetime.strptime(item.date.split('T')[0], '%Y-%B-%D')
        # item['text'] = [text.strip() for text in item.text]
        return item
