import json

import scrapy


class MyeduSpider(scrapy.Spider):
    name = 'myedu'
    allowed_domains = ['amirulislam.zeet.app']
    start_urls = ['http://amirulislam.zeet.app/']

    def parse(self, response):
        code = response.css('div.container div.row div.timeline-centered')
        labels = code.xpath('//div[@class="timeline-label"]/text()').getall()
        
        return {"response": len(labels)}
        # with open("a.json", 'wb') as f:
        #     f.write(response.body)
        # with open("b.json", 'wb') as f:
        #     f.write(json.dumps({"title": title}))
        # self.log(f'Saved file a.json')
