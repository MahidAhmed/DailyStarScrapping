import scrapy

class DailyStarSpider(scrapy.Spider):
    name = 'dailyStar'
    start_urls = [
        'https://www.thedailystar.net/'
    ]

    def parse(self, response):
        heading = response.css("h3.title a").xpath("@href").extract()
        yield {'heading of news':heading}