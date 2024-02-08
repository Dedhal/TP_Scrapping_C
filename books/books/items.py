# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksItem(scrapy.Item):
    # define the fields for your item here like:
    titre = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    category = scrapy.Field()
    rating = scrapy.Field()
    description = scrapy.Field()
    image_url = scrapy.Field()
    # url = scrapy.Field()
    
    pass
