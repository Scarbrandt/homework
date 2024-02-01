# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WikiItem(scrapy.Item):
    title = scrapy.Field()
    director = scrapy.Field()
    year = scrapy.Field()
    genre = scrapy.Field()
    country = scrapy.Field()
