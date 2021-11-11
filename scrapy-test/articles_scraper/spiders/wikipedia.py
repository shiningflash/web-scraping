import scrapy
from articles_scraper.items import Article
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class WikipediaSpider(CrawlSpider):
    name = 'wikipedia'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Taylor_Swift']
    
    custom_settings = {
        "FEED_URI": "articles.csv",
        "FEED_FORMAT": "csv"
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
        article['lastUpdated'] = response.xpath('//li[@id="footer-info-lastmod"]/text()').get().strip()
        return article
