import scrapy

from xiaomi.items import XiaomiItem

class XiaomiSpider(scrapy.Spider):
	name = 'xiaomi'
	allowed_domains = ['mi.com']
	start_urls = ['http://app.mi.com']

	def parse(self, response):
		for sel in response.xpath('//ul[@class = "applist"]/li/h5/a'):
			item = XiaomiItem()
			# print (sel.xpath('text()').extract())
			item['name'] = sel.xpath('text()').extract()
			yield item


		# filename = 'test.txt'
		# with open(filename,'wb') as f:
		# 	f.write(response.body)
