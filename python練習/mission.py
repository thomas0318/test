# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 22:31:06 2018

@author: Thomas
"""

import requests
import json
from bs4 import BeautifulSoup
page_html = requests.get("https://www.google.com/maps/d/u/0/viewer?mid=16CPoRpngieDgfTW0IqP_0hm6lgzZq_EE&ll=25.151555455329866%2C121.3529242799716&z=14")
bs = BeautifulSoup(page_html.content,'html.parser')
main_content = bs.find('div',{'class':'HzV7m-pbTTYe-ibnC6b-V67aGc'})
print(main_content)