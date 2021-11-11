import scrapy


class Article(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    lastUpdated = scrapy.Field()


class NewsArticle(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()
    source = scrapy.Field()
    date = scrapy.Field()
    author = scrapy.Field()
    text = scrapy.Field()
