# Article Scraper using Scrapy

## Overview
This directory contains a Scrapy-based project for web scraping articles from sources like Wikipedia and Yahoo News. It demonstrates how to create and manage web crawlers effectively while adhering to best practices.

---

## Requirements

To install Scrapy, use the following command:
```bash
pip3 install scrapy
```

---

## Commands

### Creating a New Scrapy Project
To create a new Scrapy project, run:
```bash
scrapy startproject <project-name> .
```

### Generating a New Spider
To generate a new spider, use:
```bash
scrapy genspider <spider-name> <url>
```

---

## Running the Spider

Navigate to the `spiders` folder and run:
```bash
scrapy runspider wikipedia_spider.py -o <filename> -t <file-format> -s <settings_attr_name>=<value>
```

### Example
To save the response in a CSV file:
```bash
scrapy runspider wikipedia_spider.py -o articles.csv -t csv -s CLOSESPIDER_PAGECOUNT=10
```

---

## Notes

1. `-s`: Specifies settings. For instance, `CLOSESPIDER_PAGECOUNT` can be defined in `settings.py` instead of the command line.
2. `-o`: Specifies the output file. This can also be configured in `settings.py` using:
   ```python
   FEED_URI = <filename>
   ```
3. `-t`: Specifies the output format (e.g., CSV, JSON, XML). This can also be configured in `settings.py` using:
   ```python
   FEED_FORMAT = <format>
   ```
4. Custom settings can be added inside spiders:
   ```python
   custom_settings = {
       "FEED_URI": "articles.json",
       "FEED_FORMAT": "json"
   }
   ```

---

## Tips

1. Use `ITEM_PIPELINES` in the `settings.py` file for data processing.
2. Always set `ROBOTSTXT_OBEY = True` in the `settings.py` file to respect the `robots.txt` directives of websites.

---

## Best Practices

- Implement pagination handling for better data coverage.
- Use robust error handling for HTTP requests and parsing.
- Store extracted data in structured formats like JSON or CSV for downstream analysis.

---

## Contact

**Author**: Amirul Islam Al Mamun
**GitHub**: [shiningflash](https://github.com/shiningflash)
