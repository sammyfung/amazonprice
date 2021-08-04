import scrapy
import re
from datetime import datetime
from amazonprice.items import AmazonpriceItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?k=ASTM+Level+3&ref=nb_sb_noss']
    url_prefix = 'https://www.amazon.com'

    def parse(self, response):
        if not re.search('\&page=', response.url):
            # Looking for number of pages if it is the first page.
            pager = response.xpath('//div[contains(@class, "a-section")]/span[contains(@class, "widgetId=pagination-button")]/div/span/text()').extract()
            if len(pager) == 0:
                pager = response.xpath('//div[contains(@class, "a-section")]/span[contains(@class, "widgetId=pagination-button")]/div/span/span/text()').extract()
            if len(pager) == 0:
                pager = response.xpath('//div[contains(@class, "a-section")]/span[contains(@class, "widgetId=pagination-button")]/div/ul/li/text()').extract()
            try:
                pages = int(pager[len(pager)-1])
                for i in range(1, pages+1):
                    url = response.url + '&page=%s' % (i)
                    yield scrapy.Request(url, callback=self.parse_items)
            except:
                pager = response.xpath('//div[contains(@class, "a-section")]/span[contains(@class, "widgetId=pagination-button")]/div').extract()
                print('exception found.')
                print(pager)

    def parse_items(self, response):
        items = []
        results = response.xpath('//div[contains(@class, "s-search-results")]/div[contains(@class, "s-result-item")]')
        items_count = 0
        for i in results:
            item = AmazonpriceItem()
            item['data_time'] = datetime.now()
            try:
                # Looking for Item HTML Pattern 1
                details = i.xpath('div[contains(@class, "sg-col-inner")]/span/div/div/div[2]/div[2]/div/div/div')
                if len(details) < 3:
                    # Looking for Item HTML Pattern 2
                    details = i.xpath('div[contains(@class, "sg-col-inner")]/span/div/div/div/div[2]/div[2]/div/div/div')
                if len(details) < 3:
                    # Looking for Item HTML Pattern 3
                    details = i.xpath('div[contains(@class, "sg-col-inner")]/span/div/div/div/div/div[2]/div[2]/div/div/div')
                # Get the item details if an item found.
                if len(details) == 3:
                    item['title'] = details[0].xpath('h2/a/span/text()').extract()[0]
                    item['url'] = self.url_prefix + details[0].xpath('h2/a/@href').extract()[0]
                    prices = details[2].xpath('div/div/div[1]/div/a/span/span[1]/text()').extract()
                    if len(prices) > 0:
                        # Price
                        try:
                            item['price'] = float(re.sub('[\$,]', '', prices[0]))
                        except:
                            # For unavailable items, price will be marked as 0.
                            item['price'] = 0
                    else:
                        # For unavailable items, price will be marked as 0.
                        item['price'] = 0
                    items.append(item)
                    items_count += 1
            except:
                print('exception found on parsing items.')
        return items

