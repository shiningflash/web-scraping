## Web-scraping using _scrapy_

### Requirements

To install scrapy, `$ pip3 install scrapy`

### Command

To create new scrapy project: `$ scrapy startproject <project-name> .`

To generate new spider: `$ scrapy genspider <spider-name> <url>`

### RUN

To run the spider: go to the `spiders` folder and run `$ scrapy runspider wikipedia.py -o articles.json -t json -s CLOSESPIDER_PAGECOUNT=10`.

To save response in csv file, `$ scrapy runspider wikipedia.py -o articles.csv -t csv -s CLOSESPIDER_PAGECOUNT=10`
