import scrapy
import somespider

class MainSpider(scrapy.Spider):
    name = "lab1main"
    start_urls = ["http://uartlib.org/"]
    
    def parse(self, response):
        for x in range(20):
            xml = somespider.Parse(somespider.self, response, xml)
