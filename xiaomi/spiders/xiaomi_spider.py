import scrapy

from xiaomi.items import XiaomiItem

from scrapy_splash import SplashRequest

from scrapy.linkextractors import LinkExtractor

class XiaomiSpider(scrapy.Spider):
	name = 'xiaomi'
	allowed_domains = ['mi.com']
	start_urls = ['http://app.mi.com']

	def parse(self, response):
		le = LinkExtractor()
		for link in le.extract_links(response):
			yield SplashRequest(
				link.url, 
				self.parse_dir_contents,
				endpoint='render.html',
				args={'wait':0.5}
				)

	# def pares(self, response):
	# 	for href in response.css("div.main-h > a"):
	# 		url = response.urljoin(href.extract())
	# 		yield scrapy.Request(url, callback=self.parse_dir_contents)


	def parse_dir_contents(self, response):
		for sel in response.xpath('//ul[@class = "applist"]/li/h5/a'):
			item = XiaomiItem()
			# print (sel.xpath('text()').extract())
			item['name'] = sel.xpath('text()').extract()
			yield item


		# filename = 'test.txt'
		# with open(filename,'wb') as f:
		# 	f.write(response.body)
