# -*- coding: utf-8 -*
"""
Created on Fri Feb  2 20:22:59 2018

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

content = soup.find(id="main-content").text
target_content = u'※ 發信站: 批踢踢實業坊(ptt.cc),'
#去除掉 target_content
content = content.split(target_content)
#print(content)
content = content[0].split(date)
#print(content)
#去除掉文末 --
main_content = content[1].replace('--', '')
#印出內文
print(main_content)

data2 = "內文:"
data3 = "推文:"

for push in pushes:
    push.extract()
for push in pushes:
            
            push_userid = push.find('span', 'push-userid').string.strip(' \t\n\r')
          
            push_content = push.find('span', 'push-content').strings
            push_content = ' '.join(push_content)[1:].strip(' \t\n\r')  
            push_ipdatetime = push.find('span', 'push-ipdatetime').string.strip(' \t\n\r')
            messages.append( {"推文作者": push_userid, "推文內容": push_content, "推文時間": push_ipdatetime} )            
            
       

data = {
        title1 : title,
        author1: author,
        date1: date,
        data2: main_content,
        data3: messages
        
     
        
        
        
        
        
      }
json.dumps(data, sort_keys=False)
print(data)
    
    

        

