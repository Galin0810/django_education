import json

import scrapy
from startups_e27.items import StartupsE27Item


class SturtupsUrls(scrapy.Spider):
    name = "startups_e27"
    allowed_domains = ["e27.co"]
    api_url = 'https://e27.co/startups/load_startups_ajax?all&per_page={}&append=1'

    def start_requests(self):
        for i in range(1532):
            yield scrapy.Request(self.api_url.format(i), callback=self.parse, dont_filter=True)

    def parse(self, response):
        data = json.loads(response.body.decode())
        selector = scrapy.Selector(text=data['pagecontent'])
        company_profile_urls = selector.xpath('//*[@id="startup-list"]/div[2]/div/div[1]').extract()
        for i in company_profile_urls:
            item = StartupsE27Item(url=i)
            yield item
