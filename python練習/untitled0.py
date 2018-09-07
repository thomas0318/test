# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 20:18:52 2018

@author: Thomas
"""

import requests
from bs4 import BeautifulSoup
context ={}
push_userid = []
page_html = requests.get("https://www.ptt.cc/bbs/joke/M.1517570799.A.1C8.html")
soup = BeautifulSoup(page.html.text)