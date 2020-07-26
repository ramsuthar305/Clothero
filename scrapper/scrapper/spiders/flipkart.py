import scrapy
from scrapy.selector import Selector
import pandas as pd
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dress_search_engine"]
mycol = mydb["data"]

class QuotesSpider(scrapy.Spider):
    name = "flipkart"

    def start_requests(self):
        urls = 'https://www.flipkart.com/mens-tshirts/pr?sid=clo%2Cash%2Cank%2Cedy&otracker[]=categorytree&otracker[]=nmenu_sub_Men_0_T-Shirts&page='
        for page in range(20):
            yield scrapy.Request(url=urls+str(page), callback=self.parse)

    def parse(self, response):
        items = response.css(".IIdQZO").extract()
        item_data = []
        for i in items:
            name = Selector(text=str(i)).css('._2mylT6::text').get()
            price = Selector(text=str(i)).css('._1vC4OE::text').get()
            product_link = 'https://www.flipkart.com' + \
                Selector(text=i).css('._2mylT6::attr(href)').extract_first()
            product_image = Selector(text=str(i)).css(
                '._3togXc::attr(src)').extract_first()
            insert_status = mycol.insert_one(
                {'name': name, 'price': price, 'product_link': product_link, 'image': product_image, 'company': 'Flipkart', 'type': 'tshirt'})
            
            #code for creating csv
        #     item_data.append([name, price, product_link, product_image])
        # if len(item_data):
        #     df = pd.DataFrame(item_data, columns=[
        #                       'Name', 'Price', 'Product Link'])
        #     df.to_csv('flipkart.csv', mode='a')
        #     print(df)
