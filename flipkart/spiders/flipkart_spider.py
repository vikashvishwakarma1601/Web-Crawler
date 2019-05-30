import scrapy
import json

class MySpider(scrapy.Spider):

	name = "flipkart_spider"

	start_urls = [
		'https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0&otracker1=AS_Query_TrendingAutoSuggest_1_0&as-pos=1&as-type=TRENDING&page=1',
		]


	def parse(self,response):
		
		data_all = response.css("div.bhgxx2")
		
		filename = "file.json"
		for data in data_all:
			mobile_name = data.css('div._3wU53n::text').get()
			rating = data.css('div.hGSR34::text').get()
			price = data.css('div._1vC4OE::text').get()
		

			if(mobile_name is not None and rating is not None and price is not None):
				y = {
		 		'Mobile':mobile_name,
		 		'Rating':rating,
		 		'Price':price,
		 		}
				with open(filename,'a') as f:
					json.dump(y,f)
					f.write("\n")


		next_page_id = response.css("nav._1ypTlJ a._3fVaIS::attr(href)").get()
		if next_page_id is not None:
			next_page = response.urljoin(next_page_id)
			print(next_page)
			yield scrapy.Request(url=next_page,callback=self.parse)

