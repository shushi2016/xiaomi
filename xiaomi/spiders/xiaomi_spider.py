from scrapy.spiders import CrawlSpider, Rule
from xiaomi.items import XiaomiItem
from scrapy_splash import SplashRequest
from scrapy.linkextractors import LinkExtractor


rules = (
		Rule(LinkExtractor(allow='\.\.\.?page=[0-9]*')),
		)

class XiaomiSpider(CrawlSpider):
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

	def parse_dir_contents(self, response):
		for sel in response.xpath('//ul[@class = "applist"]/li/h5/a'):
			item = XiaomiItem()
			# print (sel.xpath('text()').extract())
			item['name'] = sel.xpath('text()').extract()
			yield item
