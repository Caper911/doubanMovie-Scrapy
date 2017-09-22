# -*- coding: utf-8 -*-

#####Target Url
#All Movie
##https://movie.douban.com/j/search_subjects?type=movie&tag=热门&sort=rank&page_limit=20&page_start=200

##Movie digital
#https://movie.douban.com/j/subject_abstract?subject_id=26270502

##Movie Tag
#https://movie.douban.com/j/search_tags?type=movie

import scrapy
import json


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ['https://movie.douban.com/j/search_tags?type=movie/']
    tag = '热门'
    type_ = 'movie'
    page_limit = '80'
    page_start = 1
    subject_id = ''
    tag_list= []

    def parse(self, response):
        self.tag_list = json.loads(response.text)
        print(self.tag_list['tags'])
        for item in self.tag_list['tags']:
            self.tag = item
