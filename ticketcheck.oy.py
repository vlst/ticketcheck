__author__ = 'tim.postlewaite'

import urllib.request
from bs4 import BeautifulSoup


responseFile = 'response.html'
site = 'http://prime.paxsite.com/registration'

response = urllib.request.urlopen(site)

html = response.read()

f = open(responseFile, 'w')

f.write(str(html))
