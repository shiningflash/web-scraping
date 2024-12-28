import json

import scrapy
from articles_scraper.items import NewsArticle
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


# must change it scrapy.Spider to CrawlSpider
class YahooSpider(CrawlSpider):
    name = 'yahoo'
    allowed_domains = ['news.yahoo.com']
    start_urls = ['http://news.yahoo.com/']
    
    # optional
    custom_settings = {
        "FEED_URI": "news.json",
        "FEED_FORMAT": "json",
        "CLOSESPIDER_PAGECOUNT": 10
    }
    
    rules = [
        Rule(
            LinkExtractor(allow=r'\/[a-zA-Z\-]+-[0-9]+.html'),
            callback='parse_item',
            follow=True
        )
    ]

    def parse_item(self, response):
        article = NewsArticle()
        article['url'] = response.url
        article['source'] = 'Yahoo News'
        
        jsonData = json.loads(response.xpath('//article[@role="article"]/script[@type="application/ld+json"]/text()').get())
        article['title'] = jsonData['headline']
        article['description'] = jsonData["description"]
        article['date'] = jsonData['datePublished']
        article['author'] = jsonData["author"]["name"]
        article['text'] = response.xpath('//div[@class="cass-body"]/p/text()').getall()
        return article
