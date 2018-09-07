import jieba
f=open('fb_text.txt', encoding='utf-8-sig', errors='ignore')
lines=f.readlines()
f.close()
sentence=""
for xx in lines:
    sentence=sentence+xx

words=jieba.cut(sentence,cut_all=False)

results=""
for w in words:
    results = results + w + "\n"

f = open('result.txt','w',encoding='utf-8-sig', errors='ignore')
f.write(results)
f.close()
