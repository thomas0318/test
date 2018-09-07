# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 14:10:43 2018

@author: Thomas
"""

from lxml import etree, html  
import requests, json  
def main():
    result = requests.get("https://pokemon.gameinfo.io/zh-tw/pokemon/1-bulbasaur")
    result.encoding='utf8'
    root = etree.fromstring(result.content, etree.HTMLParser())
    for row in root.xpath("//div[@class='moves compact']/tr[position()]"):
        cc = row.xpath("./td/text()")
    print(cc)
   
   
if __name__ == "__main__":  
    main()