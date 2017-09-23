# -*- coding: utf-8 -*-
import scrapy
from noticias.items import NoticiasItem

class TecnoblogSpider(scrapy.Spider):
    name = 'Tecnoblog'
    allowed_domains = ['tecnoblog.net']
    start_urls = ['https://tecnoblog.net/']

    def parse(self, response):

      for article in response.css("article"):
        link    = article.css("div.texts h2 a::attr(href)").extract_first()

        yield response.follow(link, self.parse_article)

      next_page = response.css('a#mais::attr(href)').extract_first()
      if next_page is not None:
          yield response.follow(next_page, self.parse)

    def parse_article(self, response):
      link   = response.url
      title  = response.css("title ::text").extract_first()
      author = response.css("span.author ::text").extract_first()
      text   =  "".join(response.css("div.entry ::text").extract())

      notice = NoticiasItem(title=title, author=author, text=text, link=link)
      yield notice


