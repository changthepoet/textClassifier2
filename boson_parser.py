#encoding:utf-8
from __future__ import print_function, unicode_literals

import re

from bosonnlp import BosonNLP
import pandas as pd

coma = ['/ROOT','/SBJ','/OBJ','/PU','/TMP','/LOC','/MNR','/POBJ','/PMOD'
        ,'/NMOD','/VMOD','/VRD','/DEG','/DEV','/LC','/M','/AMOD','/PRN',
        '/CS','/DEC','/VC','/COOR']
# 注意：在测试时请更换为您的API Token
def boson_paser(s):
    nlp = BosonNLP('F0M7mzYq.14685.YvqU_Dxkya99')

    # s = ['司机13318757313来电表示提现未到帐，已告知会有延迟到账的现象','司机来电咨询订单状态 已告知乘客取消订单。','司机来电表示乘客飞机晚点，询问等待费用的情况，坐席已告知。']

    result = nlp.depparser(s)

    # t = open('12.txt')
    a = ' '.join('%s/%s' % it for it in zip(result[0]['word'], result[0]['role']))
    b = a.encode('utf8')
    return b


# print(' '.join(result[0]['tag']))
# print(result[0]['head'])
# print(' '.join(result[2]['role']))

df = pd.read_excel('excel/c1.xlsx')
t = df.content.tolist()
u = []
for a in t:
    a = a.encode('utf8')
    a = re.sub(r'\s+',' ',a) # trans多空格to空格
    a = re.sub(r'\n',';',a) # trans换行to空格
    a = re.sub(r'\t',' ',a) # trans Tab to空格
    a = a.strip(';')
    if '。' not in a or not a.endswith('。'):
        a = a + '。'
    u.append(a)
spliter = []
for i in range(0, len(u), 12):
    if len(u) - i >= 12:
        li = '$'.join(u[i:i + 12])
        ali = boson_paser(li)
        ali = ali.split('$')
        for d in ali:
            if d in coma:
                ali.remove(d)
        for d in ali:
            print (d,'\n')
        spliter.extend(ali)
    else:
        li1 = '$'.join(u[i:])
        ali1 = boson_paser(li1)
        ali1 = ali1.split('$')
        for d in ali1:
            if d in coma:
                ali1.remove(d)
        for p in ali1:
            print (p,'\n')
        spliter.extend(ali1)
df['content'] = spliter
writer = pd.ExcelWriter('excel/d1.xlsx')
df.to_excel(writer, 'sheet1')
writer.save()
