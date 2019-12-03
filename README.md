# Quotes_Bot
This is a Scrapy project which aims to scrape data from different websites.

### Quotes_spider
This spider scrapes quotes from famous people from the website (http://quotes.toscrape.com)
Scraped data is stored in csv format in a file named **quotes.csv**

### Author_spider
This spider scrapes information about author who have said the quotes in the website (http://quotes.toscrape.com)
Scraped data is stored in csv format in a file names **author.csv**

### Running the spider
You can run a spider using the `scrapy crawl` command, such as:
```python
$ scrapy crawl spider_name
```
If you want to save the scraped data to a file, you can pass the -o option:
```
$ scrapy crawl spider_name -o file_name.csv
```
