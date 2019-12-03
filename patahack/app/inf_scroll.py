##
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import sys
import unittest, time, re
from get_bs import *
##
url = 'https://wornwear.patagonia.com/shop/mens'
options = Options()
options.headless=True
#browser = webdriver.Firefox(options=options)
##
def inf_scroll(url):

    """
    Uses Selenium to scroll to the bottom of an infinite-scrolling website
    and then BeautifulSoup to pull the source data.
    """
    #url = ('https://wornwear.patagonia.com/shop/mens')
    # set selenium to headless mode
    options = Options()
    options.headless=True
    browser = webdriver.Firefox(options=options)

    #get the url we want
    browser.get(url)

    #Selenium script to scroll to the bottom, wait 3 seconds, continue
    len_page = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var len_page=document.body.scrollHeight;return len_page;")
    match=False
    while(match==False):
        lastCount = len_page
        time.sleep(3)
        len_page = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var len_page=document.body.scrollHeight;return len_page;")
        if lastCount==len_page:
            match=True

    # now that we've scrolled the whole page, grab the source code
    source_data = browser.page_source

    # toss them data into the Soup!
    bs_data = BeautifulSoup(source_data, 'html.parser')
    return(bs_data)

##

if __name__ == '__main__':
    inf_scroll()
