# -*- coding: utf-8 -*-
import scrapy


class QuotesSpiderSpider(scrapy.Spider):
    name = 'quotes_spider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield{
                'text' : quote.css("span.text::text").get(),
                'author' : quote.css("small.author::text").get(),
                'tags' : quote.css("div.tags a.tag::text").getall(),
            }
