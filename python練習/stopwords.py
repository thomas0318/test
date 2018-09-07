with open('stopwords.txt', errors='ignore') as f:
    stopwords = f.read().splitlines()

for linetest in stopwords:
    print(linetest)
    
final=""
lines = open('result.txt','r',encoding='utf-8-sig', errors='ignore')
for line in lines:
    if line.replace('\n','') in stopwords:
        continue
    elif line.replace('\n','').strip()=='':
        continue
    else:
        final=final+line
        
f = open('final.txt','w',encoding='utf-8-sig', errors='ignore')
f.write(final)
f.close()

