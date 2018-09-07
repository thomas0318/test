# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 19:21:24 2018

@author: Thomas
"""

import requests
import json
from bs4 import BeautifulSoup
context = {}

page_html = requests.get("https://www.ptt.cc/bbs/joke/M.1517570799.A.1C8.html")
soup = BeautifulSoup(page_html.text)
main_content = soup.find(id="main-content")
metas = main_content.select('div.article-metaline')
messages = []
pushes = main_content.find_all('div', class_='push')
meta = main_content.select('div.article-metaline-right')
author = ''
title = ''
date = '' 

if metas:
    author1 = metas[0].select('span.article-meta-tag')[0].string 
    title1 = metas[1].select('span.article-meta-tag')[0].string
    date1 = metas[2].select('span.article-meta-tag')[0].string 
if metas:
    author = metas[0].select('span.article-meta-value')[0].string 
    title = metas[1].select('span.article-meta-value')[0].string
    date = metas[2].select('span.article-meta-value')[0].string 

    print (title1,title)
    print (author1,author)
    print (date1,date)
sort1 = meta[0].select('span.article-meta-tag')[0].string 
sort =  meta[0].select('span.article-meta-value')[0].string 
print(sort1,sort)  

content = soup.find(id="main-content").text
target_content = u'※ 發信站: 批踢踢實業坊(ptt.cc),'

content = content.split(target_content)

content = content[0].split(date)

main_content = content[1].replace('--', '')

print(main_content)
