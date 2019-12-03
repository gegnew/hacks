from flask import Flask
from config import Config
#from bs4 import BeautifulSoup

app = Flask(__name__)
app.config.from_object(Config)

# switched to selenium from requests, due to scrolling issues
#url = 'https://wornwear.patagonia.com/shop/mens'
#soup = inf_scroll(url)
# TODO: run inf_scroll() on initialization
# for now, import wornwear.html

from app import routes
