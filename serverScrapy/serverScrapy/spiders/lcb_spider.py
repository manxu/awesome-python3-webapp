import scrapy


class LcbSpider(scrapy.Spider):
    name = "lcb"
    allowed_domains = [""]
    start_urls = ["http://localhost:8082/assets"]

    def parse(self, response):
        title = response.xpath('/html/body/h1/text()')
        print(title.extract())

