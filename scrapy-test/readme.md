## Web-scraping using _scrapy_

### Requirements

To install scrapy, `$pip3 install scrapy`

### RUN

To run the spider: go to the `spiders` folder and run `$ scrapy runspider wikipedia.py -o articles.json -t json -s CLOSESPIDER_PAGECOUNT=10`.

To save response in csb file, `$ scrapy runspider wikipedia.py -o articles.csv -t csv -s CLOSESPIDER_PAGECOUNT=10`
