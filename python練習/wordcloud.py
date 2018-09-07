wd={}
lines = open('final.txt','r',encoding='utf-8-sig', errors='ignore')
for line in lines:
    if wd.get(line.replace('\n', '')) == None:
        wd[line.replace('\n', '')] = 1
    else:
        wd[line.replace('\n', '')]=wd.get(line.replace('\n', ''))+1
              
from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts
from operator import itemgetter

swd = sorted(wd.items(), key=itemgetter(1), reverse=True)
swd = swd[1:50]

tags = make_tags(swd, minsize=1,maxsize=50)
create_tag_image(tags, 'wordcloud.png', background=(0, 0, 0, 255), size=(600, 400), fontname='msjhbd')
