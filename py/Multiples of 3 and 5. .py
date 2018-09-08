# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 19:04:03 2018

@author: Thomas
"""

sum = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i 
print(sum)
