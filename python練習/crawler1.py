# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 16:37:56 2018

@author: Thomas
"""
import pymysql
import requests
import json
from bs4 import BeautifulSoup
skill={}
page_html = requests.get("https://pokemon.gameinfo.io/zh-tw/pokemon/111")
bs = BeautifulSoup(page_html.content,'html.parser')
soup = BeautifulSoup(page_html.text)
pokename = bs.find('h1',{'class':'mobile-only mobile-title'})
for name in pokename:
    print(name.strip())
img_list =bs.find('div',{'class':'images'}).findAll('img')  
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
        "pokename" : name,
        "picture" : img_src, 
        "picture_shiny" : img_src1,
        "skill_attack" : s, 
        "skill_attack1" : k,
        "skill_defence" : i, 
        "skill_defence1" : l
      }
json.dumps(data, sort_keys=False)
print(data)

db = pymysql.connect("localhost","root","","skill") # 連結資料庫 
cursor = db.cursor() 
cursor.execute("SELECT * FROM main")   # 執行 MySQL 查詢指令 
results = cursor.fetchall()      # 取回所有查詢結果 
for nest in results:           # 輸出結果 
    pokename = nest[0]
print(pokename)
      