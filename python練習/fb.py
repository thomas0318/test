# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 13:52:29 2018

@author: Thomas
"""

import requests
import json
import urllib
TOKEN = '1004732612999163|3e980299b9730222bf48d0a211b546ee'
pathname = "46251501064"
url = "https://graph.facebook.com/"+ pathname + "?"
mydict = {'fields':'posts','access_token':TOKEN}
qstr = urllib.parse.urlencode(mydict)
res = requests.get(url+qstr)
print(url+qstr)
jd = json.loads(res.text)
print (jd)
fb_text = ''
if 'posts' in jd:
    for post in jd['posts']['data']:
        if 'message' in post:
            fb_text += post['message'] + '\n'
print (fb_text)
f = open('fb_text.txt','w',encoding='utf8')
f.write(fb_text)
f.closed