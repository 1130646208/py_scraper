import scrapy
from tutorial.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['dmozdir.org']
    start_urls = [
        'http://www.dmozdir.org/Category/?SmallPath=107'
        ]

    def parse(self, response):
        sel = scrapy.selector.Selector(response)
        sites = sel.xpath('//ul[@class="listitem"]/li')
        items = []
        for site in sites:
            item = DmozItem()
            item['title'] = site.xpath('h4/@title').extract()
            item['link'] = site.xpath('h4/a/@href').extract()
            item['desc'] = site.xpath('p/text()').extract()
            items.append(item)
            
        return items
