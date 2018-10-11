import scrapy


from startups_e27.items import StartupsE27Item


class SturtupsUrls(scrapy.Spider):
    name = "sturtups_e27"
    allowed_domains = ["e27.co"]
    start_urls = ['https://e27.co/startups']

    def parse(self, response):
        item = StartupsE27Item()
        request_company_url = response.xpath('//*[@id="startup-list"]/div[2]/div/div[1]').extract()
        item["request_company_url"] = request_company_url

        yield item
