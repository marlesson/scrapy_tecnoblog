# -*- coding: utf-8 -*-
import scrapy


class TecmundoSpider(scrapy.Spider):
    name = 'Tecmundo'
    allowed_domains = ['https://www.tecmundo.com.br/noticias']
    start_urls = ['http://https://www.tecmundo.com.br/noticias/']

    def parse(self, response):
        pass
