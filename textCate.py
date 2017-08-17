#encoding:utf-8
import pandas as pd

from wordPre import *

df=pd.read_excel('excel/final_train.xlsx')
t = df.content.tolist()
u = []
for a in t:
    a = str(a)
    a = a.encode('utf8')
    u.append(a)
spliter = []
for i in range(0,len(u),100):
    if len(u) - i>=100:
        spliter.extend(wordsplit(u[i:i+100]))
    else:
        spliter.extend(wordsplit(u[i:]))
df['content'] = spliter
writer = pd.ExcelWriter('excel/split_train.xlsx')
df.to_excel(writer,'sheet1')
writer.save()

