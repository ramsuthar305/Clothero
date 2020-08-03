import scrapy
from scrapy.selector import Selector
import pandas as pd
# import pymongo
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["dress_search_engine"]
# mycol = mydb["data"]


class QuotesSpider(scrapy.Spider):
    name = "amazon"

    def start_requests(self):

        # urls = {

        #     {"type": "jeans", "link": 'https://www.amazon.in/T-Shirts-Polos-Men/s?rh=n%3A1968120031&page='},

        #     {"type": "tshirt", "link": "https://www.amazon.in/s/ref=mega_sv_s23_2_1_1_5?rh=i%3Aapparel%2Cn%3A1571271031%2Cn%3A!1571272031%2Cn%3A1968024031%2Cn%3A1968076031&ie=UTF8&lo=apparel"},

        #     {"type": "shoes", "link": "https://www.amazon.in/b?node=1983519031&ref=mega_sv_s23_2_2_1_2"},

        #     {"type": "watch", "link": "https://www.amazon.in/s?i=watches&bbn=2563504031&rh=n%3A1350387031%2Cn%3A%211350388031%2Cn%3A2563504031%2Cp_n_material_browse%3A1480914031&lo=image&hidden-keywords=-sponsored&ref=mega_sv_s23_2_3_1_2"},

        #     {"type": "sunglass", "link": "https://www.amazon.in/s/ref=mega_sv_s23_2_3_3_2?rh=i%3Aapparel%2Cn%3A1968036031&ie=UTF8&lo=apparel"},

        #         }

        # }
        urls = 'https://www.amazon.in/T-Shirts-Polos-Men/s?rh=n%3A1968120031&page='
        for page in range(200):
            yield scrapy.Request(url=urls+str(page), callback=self.parse)

    def parse(self, response):
        items = response.css(".s-asin").extract()
        #items = response.css(".s-latency-cf-section").extract()
        item_data = []
        for i in items:
            name = Selector(text=str(i)).css('.a-size-base-plus::text').get()
            price = Selector(text=str(i)).css('.a-price-whole::text').get()
            product_link = 'https://www.amazon.in' + Selector(text=i).css(
                '.rush-component a::attr(href)').extract_first()
            #product_link = 'https://www.amazon.in' + Selector(text=i).css(
            #        '.a-link-normal a::attr(href)').extract_first()
            product_image=Selector(text = str(i)).css(
                '.s-image::attr(src)').extract_first()
            # insert_status = mycol.insert_one(
            #   {'name': name, 'price': price, 'product_link': product_link, 'image': product_image, 'company': 'Amazon','type':'tshirt'})

            # code for creating csv
            item_data.append([name, price, product_link, product_image,'tshirt'])

        if len(item_data):
            df = pd.DataFrame(item_data, columns=[
                              'Name', 'Price', 'Product Link', 'Image','type'])
            df.to_csv('amazon_data_tshirt.csv', mode='a')
            print(df)


