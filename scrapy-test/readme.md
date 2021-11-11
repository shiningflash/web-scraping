## Web-scraping using _scrapy_

### Requirements

To install scrapy, `$ pip3 install scrapy`

### Command

To create new scrapy project: `$ scrapy startproject <project-name> .`

To generate new spider: `$ scrapy genspider <spider-name> <url>`

### RUN

To run the spider: go to the `spiders` folder and run `$ scrapy runspider wikipedia.py -o articles.json -t json -s CLOSESPIDER_PAGECOUNT=10`.

To save response in csv file, `$ scrapy runspider wikipedia.py -o articles.csv -t csv -s CLOSESPIDER_PAGECOUNT=10`

Notes:

1. `-s` stands for settings and `CLOSESPIDER_PAGECOUNT` is a settings attribute. We can add the attribute to the `settings.py` file insead of passing in command lines.
2. `-o` stands for output file. We can also add this in the `settings.py`. Add the line `FEED_URI=<filename>`.
3. `-t` stands for output format. We can also add this in the `settings.py`. Add the line `FEED_FORMAT=<format>`. Format can be csv, json or whatever.
