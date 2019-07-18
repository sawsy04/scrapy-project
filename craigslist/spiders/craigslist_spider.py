import scrapy 
from craigslist.items import CraigslistItem

class CraigslistSpider(scrapy.Spider):
	name = "craigslist"
	allowed_domains = ["craigslist.org"]
	start_urls = ["https://atlanta.craigslist.org/search/cto"]
	def parse(self, response ):
		items = []
		for sel in response.xpath("//li[@class='result-row']/p"): # Because we're using XPath language, we need to specify that the paragraphs we're trying to isolate are expressed via XPath
			item = CraigslistItem()
			item['title'] = sel.xpath("./a/text()").extract() # Title text from the 'a' element. 
			item['link'] = sel.xpath("./a/@href").extract() # Href/URL from the 'a' element. 
			item['price'] = sel.xpath('./span/span[@class="result-price"]/text()').extract()[0] # Price from the result price class nested in a few span elements.
			items.append(item)
		return items # Shows scraped information as terminal output.
