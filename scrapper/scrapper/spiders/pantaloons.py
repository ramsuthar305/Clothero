import scrapy
from scrapy.selector import Selector
import pandas as pd
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dress_search_engine"]
mycol = mydb["data"]


class QuotesSpider(scrapy.Spider):
    name = "pantaloons"

    def start_requests(self):
        urls = 'https://www.pantaloons.com/c/men/t-shirts-188?source=menu&page=1&orderway=desc&orderby=position'
        for page in range(20):
            yield scrapy.Request(url=urls+str(page), callback=self.parse)

    def parse(self, response):
        items = response.css(".category-list-col").extract()
        item_data = []
        for i in items:
            name = Selector(text=str(i)).css('.brand_name::text').get()
            price = Selector(text=str(i)).css('.off_price::text').get()
            print((name,price))
            # product_link = 'https://www.amazon.in' + \
            #     Selector(text=i).css(
            #         '.rush-component a::attr(href)').extract_first()
            # product_image = Selector(text=str(i)).css(
            #     '.s-image::attr(src)').extract_first()
            # insert_status = mycol.insert_one(
            #     {'name': name, 'price': price, 'product_link': product_link, 'image': product_image, 'company': 'Amazon','type':'tshirt'})
            
            #code for creating csv
        #     item_data.append([name, price, product_link, product_image])
        # if len(item_data):
        #     df = pd.DataFrame(item_data, columns=[
        #                       'Name', 'Price', 'Product Link', 'Image'])
        #     df.to_csv('amazon_data.csv', mode='a')
        #     print(df)
