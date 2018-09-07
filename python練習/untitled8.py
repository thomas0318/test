# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:26:03 2018

@author: Thomas
"""
import requests
from bs4 import BeautifulSoup
page_html = requests.get("https://www.ptt.cc/bbs/joke/M.1517500865.A.D01.html")
soup= BeautifulSoup(page_html.text)
for item in soup.select(".push-userid"):
    print(item.string)
