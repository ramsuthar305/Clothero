
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

lof = ['men-tshirts']


def myntra_scrapper(list_of_items):

    BASE_URL = 'https://www.myntra.com/'

    browser = webdriver.Firefox()
    browser.get(BASE_URL+list_of_items[0])
    print("REached website")
    time.sleep(3)
    ul = browser.find_elements_by_class_name('product-base')
    print(ul)
    time.sleep(2)
    browser.close()


myntra_scrapper(lof)
