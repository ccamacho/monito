#!/bin/python

from bs4 import BeautifulSoup

import requests

URL = "https://www.lidl.es/es/search?query=atornilladora+taladradora+percusion+20v"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
result = soup.find(class_="result_count")
for html in result:
    if '1' in html:
        print("- NOK: There is only a product")
    else:
        print("- OK: The is more than 1 product, check: " + URL)
