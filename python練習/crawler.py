# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 14:48:11 2018

@author: Thomas
"""

import requests
import json
from bs4 import BeautifulSoup
skill={}
page_html = requests.get("https://pokemon.gameinfo.io/zh-tw/pokemon/1-bulbasaur")
bs = BeautifulSoup(page_html.content,'html.parser')
soup = BeautifulSoup(page_html.text)
img_list =bs.find('div',{'class':'images with-shinies'}).findAll('img')  
img_src = img_list[0].attrs['src']
img_src1 = img_list[1].attrs['src']
print(img_src, img_src1)
asd=bs.find('div',{'class':'grid'}).findAll('a')
s = asd[0].string
k = asd[1].string
i = asd[2].string
l = asd[3].string
print(s, k, i, l)



data = {
        "picture" : img_src, 
        "picture_shiny" : img_src1,
        "skill_attack" : s, 
        "skill_attack1" : k,
        "skill_defence" : i, 
        "skill_defence1" : l
      }


json.dumps(data, sort_keys=False)
print(data)






								
     


