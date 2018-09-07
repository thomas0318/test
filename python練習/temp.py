# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 11:13:53 2018

@author: Thomas
"""

import jieba


sentence = "獨立音樂需要大家一起來推廣，歡迎加入我們的行列！"
print ("Input：", sentence)
words = jieba.cut(sentence,cut_all = False)
print ("Output 精確模式：")
for word in words:
    print (word)
    