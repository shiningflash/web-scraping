# Web Scraping Projects

## Overview
This repository demonstrates various web scraping projects using Python libraries such as: **Beautiful Soup**, **Scrapy**, **Playwright**.

Web scraping, also referred to as screen scraping, web harvesting, or web crawling, involves automating the process of extracting data from websites. These projects focus on implementing best practices for extracting and managing structured data efficiently.

---

## Tools & Technologies

- **Python**: Core programming language used for scraping.
- **Beautiful Soup**: Library for parsing HTML and XML documents.
- **Scrapy**: Framework for building web crawlers.
- **Playwright** : open-source automation library for browser testing and web scraping
- **JSON**: Storing extracted data in structured formats.
- **Pandas**: Data manipulation and cleaning (optional, for analysis).
- **Requests**: HTTP library for interacting with web pages.
- **Git**: Version control for project collaboration.

---

### Key Directories:

1. **article_scraper**:
   - A Scrapy-based project to scrape articles from sources like Wikipedia and Yahoo News.
   - Includes spiders and configurations.

2. **flipkart_scraper**:
   - Scrapes laptop data from Flipkart.

3. **timesjobs_scraper**:
   - Scrapes job listings from TimesJobs.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shiningflash/web-scraping.git
   cd web-scraping
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Flipkart Scraper

Navigate to the `flipkart_scraper` directory and run:
```bash
python main.py
```
Output will be saved in `laptops.json`.

### Article Scraper (Using Scrapy)

Navigate to the `article_scraper` directory and follow these steps:

1. **Create a new Scrapy project**:
   ```bash
   scrapy startproject article_scraper
   ```

2. **Generate a new spider**:
   ```bash
   scrapy genspider wikipedia https://en.wikipedia.org
   ```

3. **Run the spider**:
   ```bash
   scrapy runspider spiders/wikipedia_spider.py -o articles.json -t json
   ```

   **Notes:**
   - `-o` specifies the output file.
   - `-t` specifies the output format (JSON, CSV, XML, etc.).

4. **Custom Settings in Spiders**:
   ```python
   custom_settings = {
       "FEED_URI": "articles.json",
       "FEED_FORMAT": "json"
   }
   ```

### TimesJobs Scraper

Navigate to the `timesjobs_scraper` directory and run:
```bash
python main.py
```
Output will be saved in `jobs.json`.

---

## Best Practices for Scraping

1. **Respect Robots.txt**:
   - Always set `ROBOTSTXT_OBEY = True` in `settings.py`.

2. **Use Pipelines**:
   - Process data efficiently by implementing pipelines in Scrapy projects.

3. **Use Pagination**:
   - Ensure the scraper handles multiple pages effectively.

4. **Error Handling**:
   - Implement robust error handling for HTTP requests and parsing.

5. **Data Storage**:
   - Store data in structured formats like JSON or CSV for analysis.

---

## Future Improvements

1. Implement cloud-based scraping solutions.
2. Add database support (e.g., MySQL, MongoDB) for data storage.
3. Integrate with CI/CD pipelines for automated scraping.

---

## Contact

For any inquiries or suggestions:
**Author**: Amirul Islam Al Mamun
**GitHub**: [shiningflash](https://github.com/shiningflash)
