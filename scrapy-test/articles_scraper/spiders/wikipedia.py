import scrapy
from articles_scraper.items import Article
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


# must change it scrapy.Spider to CrawlSpider
class WikipediaSpider(CrawlSpider):
    name = 'wikipedia'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Taylor_Swift']
    
    # optional
    custom_settings = {
        "FEED_URI": "articles.csv",
        "FEED_FORMAT": "csv",
        "CLOSESPIDER_PAGECOUNT": 10
    }
    
    rules = [
        Rule(
            LinkExtractor(allow=r'wiki/((?!:).)*$'),
            callback='parse',
            follow=True
        )
    ]

    def parse(self, response):
        article = Article()
        article['title'] = response.xpath('//h1/text()').get() or response.xpath('//h1/i/text()').get().strip()
        article['url'] = response.url.strip()
        article['lastUpdated'] = response.xpath('//li[@id="footer-info-lastmod"]/text()').get()
        return article
