##
#import patahack as pak
from patahack import Patahack as pak
from bs4 import BeautifulSoup

#spoon = input('where is soup?')
#soup = BeautifulSoup(open(spoon), 'html.parser')

#soup = BeautifulSoup(open('wornwear.html'), 'html.parser')

with open('wornwear.html') as fp:
    soup = BeautifulSoup(fp)

##

thingsSethWants = [
    "Nano-air",
    "M10",
    "Kniferidge",
    "Houdini",
    "Micro Puff",
    "Grade VII",
    "Hyper Puff",
    "Fezzman",
    "R1"
]


copt = pak.gucci_finder(soup)
print(copt)
##

