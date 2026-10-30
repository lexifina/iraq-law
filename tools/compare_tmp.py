import re, html, unicodedata, difflib
from rapidfuzz import fuzz
def norm(s):
    s=unicodedata.normalize('NFKC',s)
    s=re.sub('[ً-ٰٟـ‌‍‎‏‪-‮]','',s)
    s=s.replace('أ','ا').replace('إ','ا').replace('آ','ا').replace('ى','ي').replace('ة','ه')
    return re.sub(r'[^\w]','',s)
w=open('ws_ar.txt',encoding='utf8').read()
wa={}
parts=re.split(r'\n\s*المادة\s*\((\d+)\)\s*[:：]?\s*',w)
for k in range(1,len(parts),2): wa[int(parts[k])]=parts[k+1]
t=open('mu.html',encoding='utf8').read()
s=t[t.find('الديباجة'):t.find('</article>')]
s=re.sub(r'(?i)</?(p|br|li|ul|ol|div|h\d)\b[^>]*>','\n',s); s=re.sub(r'<[^>]+>','',s); s=html.unescape(s).replace('\xa0',' ')
ma={}
parts=re.split(r'\n\s*المادة\s*\(\s*(\d+)\s*\)\s*[:：]?\s*',s)
for k in range(1,len(parts),2): ma[int(parts[k])]=parts[k+1]
O=norm(open('ocr_all.txt',encoding='utf8').read())
res=[]
for n in range(1,145):
    a,b=norm(wa[n]),norm(ma[n])
    if a==b: continue
    fa=fuzz.partial_ratio(a,O); fb=fuzz.partial_ratio(b,O)
    print(n,round(fa,1),round(fb,1),'WS' if fa>fb else 'MU' if fb>fa else '=')
print('--- mu vs OCR low')
low=[]
for n in range(1,145):
    b=norm(ma[n]); 
    if len(b)<12: continue
    f=fuzz.partial_ratio(b,O); low.append((round(f,1),n,len(b)))
low.sort(); print(low[:25]); import statistics; print(statistics.mean(x[0] for x in low), sum(1 for x in low if x[0]>=97))
