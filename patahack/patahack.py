##
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import pandas as pd
import sys
import re
import unittest, time, re
from get_bs import *
#from inf_scroll import inf_scroll

class Patahack:
    """all the stuff we need to cop patagucci"""
    #def __init__(self):
    #TODO: make options to select mens, womens, etc (maybe in js?)

    #TODO: take input from website for this:


    def text_search(self, text, stuff_to_cop):
        """
        this returns True if the bs4 object has stuff we wanna cop
        """
        if any(ext in text for ext in stuff_to_cop):
            return(True)
        else:
            return(False)
    ##
    def strip_patagonia(self, list):
        try:
            list.remove('patagonia.com')
        except ValueError:
            pass
        except AttributeError:
            call_security('something is fuxed')
        return(list)

    def gucci_finder(self, soup):
        """
        This function cops your cheap gucc
        INPUT:
            soup - BeautifulSoup object, html parsed

        OUTPUT:
            good_gucc - dataframe of all the gucci you could cop
        """
        gucci = soup.find_all(class_="TileItem")
        good_gucc = []
        n=0
        for item in gucci:
            title = item.find(class_='title').get_text()
            test = self.text_search(title)
            if test == True:
                sizes = []
                for size in item.find(class_='sizes').find_all('a'):
                    sizes.append(size.get_text())
                    price = item.find(class_='price').get_text()
                    image = item.find(class_='img-wrap').img['src']
                    href = item.find('a')['href']
                    n += 1
                good_gucc.append([title, sizes, price, image, href])

        print('We got ' + str(n) + ' guccis')
        good_gucc = pd.DataFrame(good_gucc, columns=['title', 'sizes', 'price', 'image', 'href'])
        good_gucc.sizes = good_gucc.sizes.apply(lambda x: strip_patagonia(x))
        return(good_gucc)
    ##

    # to get page:
    # https://wornwear.patagonia.com/ADDRESS

    ##
