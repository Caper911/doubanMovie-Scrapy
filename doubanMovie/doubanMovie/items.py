# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    movie_id = scrapy.Field()
    rate = scrapy.Field()
    short_comment = scrapy.Field()
    directors = scrapy.Field()
    actors = scrapy.Field()
    duration = scrapy.Field()
    region = scrapy.Field()
    types = scrapy.Field()
    cover_image_url = scrapy.Field()
    digital_url = scrapy.Field()
    release_year = scrapy.Field()