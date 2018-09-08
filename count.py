# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 08:09:10 2018

@author: Thomas
"""

urls = ["http://www.google.com/a.txt","http://www.google.com.tw/a.txt","http://www.google.com/download/c.jpg","http://www.google.co.jp/a.txt","http://www.google.com/b.txt","https://facebook.com/movie/b.txt","http://yahoo.com/123/000/c.jpg","http://gliacloud.com/haha.png", ] 
 
import os
from collections import Counter
temp = []
for thing in urls:
    temp.append(os.path.basename(thing))
a = Counter(temp).most_common(3)
print(a)